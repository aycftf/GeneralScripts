##File will work off of rawTCPdump.py, but will be modified to only print DNS queries and responses.
from codecs import lookup
import os, dotenv, datetime, asyncio
import sys

from webencodings import lookup
ENVFILE = os.path.join(os.path.dirname(__file__), "Findings/env.env")
if os.path.exists(ENVFILE):
    dotenv.load_dotenv(ENVFILE)
else:
    sys.exit("Env file does not exists... %s" % (ENVFILE))
DUMP = os.getenv("OUTPUT_FILE")

class resolve():
    def __init__(self, connectionFile: str | None = None):
        self.connectionFile = connectionFile or DUMP
        if not self.connectionFile:
            sys.exit("OUTPUT_FILE not set in env (within Findings dir); cannot continue.")
        self.remotes = []
        self.parseFile()
    
    
    def parseFile(self):
            if self.connectionFile is not None:
                with open(self.connectionFile, "r", encoding="utf-8") as connFile:
                    lines = connFile.readlines()
                    for line in lines:
                        #Only look at outbound HTTP/S
                        if line.split(":")[-1].strip() == "443" or "80":
                            #Example output of parsed file: ['108.177.121.190', '23.62.76.254', '34.107.243.93', '52.182.143.213', '140.82.114.25', '142.250.125.95', '4.249.131.160', '140.82.113.22', '45.83.223.196', '140.82.112.21']
                            self.remotes.append(line.split(":")[1].strip())
            return self.remotes




class query():
    def __init__(self, connectionFile: str | None = None):
        self.connectionFile = connectionFile or DUMP
        # create a resolve instance and reuse connectionFile
        self.resolver = resolve(self.connectionFile)
        #get returned output from parsing raw dump
        self.remotes = self.resolver.remotes
    
    
    def queryAddresses(self, remotes: list | None = None):
        import socket
        self.successfulLookups = {}
        remotes = remotes or self.remotes
        for x in range(len(remotes)):
            try:
                #print("Querying %s now... \n\n" % self.remotes[x])
                lookup, _, ip = socket.gethostbyaddr(self.remotes[x])
                #print(lookup, xx, u)
                ## += due to tuple object being immutable
                #Get ip out of list obj, via calling the first index
                self.successfulLookups[lookup] = ip[0]
            except socket.herror as e:
                continue
                #print(f"Host {self.remotes[x]} could not be resolved: {e}")
            
            except Exception as eE:
                print("Error during lookup %s" % (eE))
        return self.successfulLookups




def main():
    print("Parsing file for DNS queries and responses...")
    res = resolve()
    qu = query()
    for a, b in qu.queryAddresses().items():
        print("%s resolves to %s" % (b, a))
        
        

if __name__ == "__main__":
    main()