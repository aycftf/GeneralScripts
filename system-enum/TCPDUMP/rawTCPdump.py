#Takes raw /proc/net/tcp output and parses it into a more human readable format.
import subprocess as sub
import socket, struct
import time, os
import datetime
import asyncio 
import shutil

##Get first actual function of the script first, then add the rest of the code. This is a good way to avoid getting lost in the details of the code and losing sight of the overall structure of the program.
#This is just poc
LOCO = os.getcwd()

class TcpDump:
    def __init__(self):
        self.dumpProc = self.get_tcp_dump() 
        self.dumpProcUdp = self.get_udp_dump() 
        self.parseProc = self.parseDump()

    def get_tcp_dump(self):
        #Get the raw tcp dump from /proc/net/tcp
        with open("/proc/net/tcp", "r") as f:
            return f.read()
        
        
    def get_udp_dump(self):
        #Get the raw udp dump from /proc/net/udp
        with open("/proc/net/udp", "r") as u:
            return u.read()

    #Convert a hex string to an IP address 
    #struct: Convert Python values to C structs, handle and convert to Python byte objects
    #<I: Little-endian unsigned int (4 bytes)
    #<L: Little-endian unsigned long (4 bytes)
    #inet_ntoa: Network address to ASCII
    def hex_to_ip(self, hex_ip):
        ip = socket.inet_ntoa(struct.pack("<L", int(hex_ip, 16)))
        return ip
    #Convert a hex string to a port number via 16 base conversion
    def hex_to_port(self, hex_port):
        return int(hex_port, 16)
    
    def parseDump(self):
        #Parse the raw tcp dump and return a list of dictionaries containing the relevant information
        lines = self.dumpProc.splitlines()
        linesUdp = self.dumpProcUdp.splitlines()
        #Now slice both tcp and udp, remove headers, and parse
        linelines = linesUdp[1:] + lines[1:]
        headers = lines[0].split()
        data = []
        #print(headers)
        entries = {}
        for line in linelines:
            feilds = line.split()
            #print(feilds)
            ##LOCAL ADDRESS SOCKETS
            lanSocks = feilds[1] .split(":")
            #REMOTE ADDRESS SOCKETS
            remSocks = feilds[2].split(":")
            uidofSock = feilds[7].split(":")
            ##Append all indicies from feilds, and then  split them within dictionary object
            entries = {
                #Split each entry up by indicie to count on later
                #Ex: We loop thru first dict object entry1, then in those keys and vals, we can seperate each value with cooresponding keys during loop, then directly jump to next 'entry'
                f"Entry {feilds[0]}": {
                    "local_address": self.hex_to_ip(lanSocks[0]),
                    "local_port": self.hex_to_port(lanSocks[1]),
                    "remote_address": self.hex_to_ip(remSocks[0]),
                    "remote_port": self.hex_to_port(remSocks[1]),
                    "UID of Socket": uidofSock[0]
                }
            }
            data.append(entries)
        return data
    
    #Parse and clean tcp dump info and print it in a more human readable format  
    #This function specifically looks for remote ports and services opened and listening + activley being used  
    def parseDumpRemote(self):
        final = []
        ##use set instead of list object to store seen addresses as hashes internally
        seenAddr = set() 

        for entry in self.parseProc:
            for k, v in entry.items():
                ## k == entry number, v == dictionary of local and remote address and ports
                for key, value in v.items():
                    if key == "remote_address" and v['remote_port'] != 0:
                        if value not in seenAddr and value != "127.0.0.1":
                            seenAddr.add(value)
                            key = "Listening_Connection"
                            final.append(f"{key}: {value}" + ":" + f"{v['remote_port']}")
                    
        return final
    
    def parseDumpLocal(self):
        final = []
        seenPorts = set() ##use set instead of list object to store seen ports as hashes internally

        for entry in self.parseProc:
            for k, v in entry.items():
                #k is unused, as to split each dict object up for loop
                for key, value in v.items():
                    if key == "local_address" and v['local_port'] != 0:
                        if v['local_port'] not in seenPorts:
                            seenPorts.add(v['local_port'])
                            key = "Listening_Connection"
                            final.append(f"{key}: {value}" + ":" + f"{v['local_port']}")
                    
        return final





class whoisLookup():
    def __init__(self):
        self.dump = TcpDump()
        self.remotes = self.dump.parseDumpRemote()
        self.whoisPath = shutil.which("whois")
	    #test fix of race condition from async
        #self.commWhois = sub.run(["which", "whois"], capture_output=True, text=True)
        if not self.whoisPath:
            print("whois command not found, please install whois and try again (for remote lookups).")
            print("Still logging each listening connection....")
            raise Exception("whois command not found, please install whois and try again (for remote lookups).")
    
    async def lookup(self):
        for x in range(len(self.remotes)):
            conn = self.remotes[x].split(": ")
            #Seperate ip and port to use in whois lookup
            ip, port = conn[1].split(":")
            if str(ip.strip()).startswith("192"):
                continue
            print("Checking %s on Listening Port %s"% (ip.strip(), port))
	        #Dont block event loop and just pause couroutine, also avoid rate limit
            await asyncio.sleep(1)
            #Actually run whois with subprocess, NO SHELL
            result = sub.run([str(self.whoisPath), str(ip.strip())], capture_output=True, text=True)
            #result = sub.run(["wh", str(ip.strip())], capture_output=True, text=True)
            #continue when user presses button 
            print(result.stdout)
            #Avoid looping after last entry
            if self.remotes[x] != self.remotes[-1]:
                print("Press Enter to continue to next lookup...")
                input()
		    #Sourced: https://stackoverflow.com/questions/55027940/is-run-in-executor-optimized-for-running-in-a-loop-with-coroutines
            #input_future = asyncio.get_event_loop().run_in_executor(None, input)
    
    
    async def writeOutput(self):
        dump = self.remotes
        dir = os.path.join(LOCO, "Findings")
        try:
            os.makedirs(dir, exist_ok=True)
            # perms : rwxr-xr-x
            os.chmod(dir, 0o755)  
        except Exception as e:
            print(f"Failed to create output directory {dir}: {e}")
            return
        #Get current date in string format Hour Minute Second to append to output file name
        datee = datetime.datetime.now().strftime("%H-%M-%S")
        
        #if remotes output, then write to file, else skip writing to file and print message
        if dump:
            print(f"Writing output to file located at {dir}/Raw_TCPDump_Output_{datee}.txt...")
            with open(f"{dir}/Raw_TCPDump_Output_{datee}.txt", "w") as f:
                try:
                    for r in self.remotes:
                        f.write(r + "\n")
                
                except IOError as e:
                    print("Check file permissions, failed to write output file: \n %s"% e)
                
                        
                except Exception as e:
                    print("Error writing to file: %s"% e)
            rem = input("Remove previous log files?")
            if isinstance(rem, str) and rem.lower() == "y":
                for file in os.listdir(dir):
                    if file.startswith("Raw_TCPDump_Output_") and not file.endswith(f"{datee}.txt"):
                        try:
                            os.remove(os.path.join(dir, file))
                            print(f"Removed {file}")
                        except Exception as e:
                            print(f"Failed to remove {file}: {e}")
            
            #Write an env file in new findings dir for future script use
            if not os.path.exists(f"{dir}/env.env"):
                with open(f"{dir}/env.env", "w") as f:
                    try:
                        f.write(f"LOC_OF_SCRIPT={LOCO}\n")
                        f.write(f"OUTPUT_FILE={dir}/Raw_TCPDump_Output_{datee}.txt\n")
                        f.write(f"VT_API_KEY=INSERT \n")
                        f.write(f"IDBP_API_KEY=INSERT \n")
                        f.write(f"SHOADAN_API_KEY=INSERT \n")
                        f.write(f"URLHAUSE_API_KEY=INSERT \n")
                    except IOError as e:
                        print("Check file permissions, failed to write env file: \n %s"% e)
                    except Exception as e:
                        print("Error writing to env file: %s"% e)
            


async def main():
    # instantiate once so we keep the same lookup results
    wl = whoisLookup()
    # if whois is not available, use constructor to print a message and set returncode
    #if getattr(wl, 'commWhois', None) and wl.commWhois.returncode != 0:
    #    print(wl.commWhois.stderr.strip())
    #    return
    
    #perform both lookups, and write stdout sequentially due to blocking inputs
    await wl.writeOutput()
    await wl.lookup()

if __name__ == "__main__":
    asyncio.run(main())
