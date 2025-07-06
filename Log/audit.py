
#Py script to specifically Import words from file, loop thru ...
#Then run each audit command w/ keywords


import os, time, sys, subprocess


def main():
    
    time.sleep(1)
    print("Running Log Process Now...")
    run()
    
def run():

    keywords = []
    
    #Pull user dir
    dir = os.getcwd()
    #Check if file exists from previous script in proper directory
    file = os.path.exists(f"{dir}/loop.txt")
    if file == True:
        print("Checking if proper files exist...")
        time.sleep(2)
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
            
            #For loop for words now found in loop file
            for keyWords in keywords:
                keyWords = keyWords.strip()
                time.sleep(1)
                print(f"CHECKING KEYWORD : {keyWords}")
                print("\n \n\n\n")
                time.sleep(2)
                ausearch = f"sudo ausearch -i -k {keyWords}"
                
                #Subprocess runs a command to standard output ad error to terminal
                #Optiuon shell=True: Allows shell process to be ran concurrently with live session
                #Option cap_output: captures output of the command in live term
                #Option text=True: ASCII output
                result = subprocess.run(ausearch, shell=True, capture_output=True, text=True)
                print("RESULT-FROM-KEYWORD:", result.stdout)
                print("Errors:", result.stderr)
                
                time.sleep(4)

    else:
        print(f"{dir}/loop.txt is non existent, try running again...")
        sys.exit("Bye :( ")


if __name__ == "__main__":
    main()
