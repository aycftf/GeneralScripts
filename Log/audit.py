
#Py script to specifically Import words from file, loop thru ...
#Then run each audit command w/ keywords


import os, time, sys, subprocess

LOGFILE="/var/log/audit/audit.log"
#Pull user dir
dir = os.getcwd()
LOOP=f"{dir}/loop.txt"

    
def run():
    keywords = []
    print("Checking if proper files exist...")
    time.sleep(2)
    #Check if file exists from previous script in proper directory
    file = os.path.exists(LOOP)
    if file:
        print("\n")
        print(f"{dir}/loop.txt exists! Continuing Script As Normal... ")
        time.sleep(2)
        #Open temp file made to read all keywords
        with open(f'{dir}/loop.txt', 'r') as loooop:
            #Loop thru
            for word in loooop:
                #Append all words with extend and split them to remove trailspace
                if word not in keywords:
                    keywords.extend(word.split())
                #Move onto next forloop when done
                else:
                    print("Words added to proper file!")
                    break
            
        try:
            with open(f'{dir}/loop.txt', 'r', encoding='utf-8') as opened:
            
                clearme = "clear"
                
                readme = opened.read()
                words = readme.split()
                
                if len(words) > 0 or words != ' ':
                    checked = []
                    for keyWords in words:
                        keyWords = keyWords.strip()
                        if keyWords not in checked:
                            checked.append(keyWords)
                            time.sleep(1)
                            print(f"CHECKING KEYWORD : {keyWords}")
                            print("\n")
                            time.sleep(2)
                            ##TODO TODO: MUST PIPE TO GREP -V AUDIT SEARCHES
                            ausearch = f"sudo ausearch -i -k {keyWords}"
                            
                            #Subprocess runs a command to standard output ad error to terminal
                            #Optiuon shell=True: Allows shell process to be ran concurrently with live session
                            #Option cap_output: captures output of the command in live term
                            #Option text=True: ASCII output
                            result = subprocess.run(ausearch, shell=True, capture_output=True, text=True)
                            
                            if result.stdout == None:
                                print("Nothing found from log for %s ...."% (keyWords))
                            print(result.stdout)
                            print("Errors:", result.stderr)
                            
                            time.sleep(4)
                            input("Input anything on keyboard to continue loop...")
                            os.system(clearme)
                    
                else:
                    print(f"No keywords added to {dir}/loop.txt to search for.... ")
                    time.sleep(1)
                    print("Proceeding on with regular audit check")
                    
                        
        except Exception as ff:
            sys.exit(f"{ff}")
            

    else:
        print(f"{dir}/loop.txt is non existent, try running again...")
        sys.exit("Bye :( ")



def parseKeywords():
    proctile = []
    cwd = []
    dirExe = []
    uid = []
    username = []
    time = []
    syscall = []
    if os.path.exists(LOGFILE):
        comm = "sudo /usr/sbin/auditctl -l"
        try:
            rules = subprocess.run(comm, text=True, capture_output=True, shell=True, check=True)
            print(rules.stdout, rules.stderr)
        
        except subprocess.CalledProcessError:
           pass
       
        if os.path.exists(LOOP):
                with open(LOGFILE, 'r') as logParse:
                    logRead = logParse.read().split()
                    for findKey in logRead:
                        print(findKey.strip())
    
    
    else:
        sys.exit("Dedicated log file for auditd does NOT exist? Logging to rsyslog? ")




def main():
    
    time.sleep(1)
    print("Running Log Process Now...")
    run()



if __name__ == "__main__":
    main()
