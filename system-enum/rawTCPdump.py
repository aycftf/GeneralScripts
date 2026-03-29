
#Takes raw /proc/net/tcp output and parses it into a more human readable format.
import subprocess as sub
import socket, struct
import time

##Get first actual function of the script first, then add the rest of the code. This is a good way to avoid getting lost in the details of the code and losing sight of the overall structure of the program.
#This is just poc


class TcpDump:
    def __init__(self):
        self.dumpProc = self.get_tcp_dump()
        self.parseProc = self.parseDump()

    def get_tcp_dump(self):
        #Get the raw tcp dump from /proc/net/tcp
        with open("/proc/net/tcp", "r") as f:
            return f.read()
        
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
        headers = lines[0].split()
        data = []
        #print(headers)
        entries = {}
        for line in lines[1:]:
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
        seenAddr = set() ##use set instead of list object to store seen addresses as hashes internally

        for entry in self.parseProc:
            for k, v in entry.items():
                ## k == entry number, v == dictionary of local and remote address and ports
                for key, value in v.items():
                    if key == "remote_address" and v['remote_port'] != 0:
                        if value not in seenAddr:
                            seenAddr.add(value)
                            key = "Listening_Connection"
                            final.append(f"{key}: {value}" + ":" + f"{v['remote_port']}")
                    
        return final
        '''
        fields = line.split()
        entry = {}
        for i, header in enumerate(headers):
            entry[header] = fields[i]
        data.append(entry)
    return data
    '''
    
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
        self.commWhois = sub.run(["which", "whois"], capture_output=True, text=True)
        if self.commWhois.returncode != 0:
            print("whois command not found, please install whois and try again.")
            return
    
    def lookup(self):
        for x in range(len(self.remotes)):
            conn = self.remotes[x].split(": ")
            ip, port = conn[1].split(":")
            print("Checking %s on Listening Port %s"% (ip.strip(), port))

            #Use whois command to lookup the IP address and return the result
            result = sub.run([self.commWhois.stdout.strip(), str(ip.strip())], capture_output=True, text=True)
            #result = sub.run(["wh", str(ip.strip())], capture_output=True, text=True)
            time.sleep(3) #Sleep for 3 seconds to avoid rate limiting
        
        
            print(result.stdout)


def main():
    print(whoisLookup().lookup())



if __name__ == "__main__":
    main()