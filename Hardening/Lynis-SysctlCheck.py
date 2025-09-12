import os, pdb
import sys
import subprocess
import sys
import re
import platform
import time
from params import IP4_PARAMS


#Script for sysctl Hardening Parameters and Kernal Hardening

#Documentation Surrounding different Kernal/Sysctl Params Regarding argument level / rule level:

#https://linux-audit.com/kernel/sysctl/kernel/
#Lynis audit system
#github.com/alegrey91/systemd-service-hardening/blob/master/systemd-service-hardening.pdf
#https://blog.sergeantbiggs.net/posts/hardening-applications-with-systemd/ 
#sudo systctl -A



DIR = os.getcwd()
PARAMS = IP4_PARAMS.items()
REMOVE_TRAILING_NUMS = r'\d+'

#Function to see if user runs with root perms that returns a bool
def whoami():
	return os.getuid() == 0



def whatsmyos():
	os_name = platform.system()
	if os_name == "Linux":
		try:
			ubuntu = subprocess.run(['apt-get', 'update', '-y'], text=True, check=True, capture_output=True)

			if ubuntu.returncode == 0:
				
				if os.path.exists(f"{DIR}/allsystemdservices.txt"):
					print("File exists, deleing!")

				findsystemdservices = subprocess.run(['systemd-analyze', 'security'], check=True, text=True, capture_output=True)


				if findsystemdservices.returncode == 0:
					with open('allsystemdservices.txt', 'w') as e:
						e.write(findsystemdservices.stdout)

			
		except subprocess.SubprocessError as f:
			sys.exit(f"{f}")
	
		return ubuntu.stdout
			






def getParams():
	currentParams = {}
    
	#Use subprocess.PIPE to properly pipe a file to run a command with optiosn / piping other commands
	grabSysctl = subprocess.run(['sysctl', '-A'], stdout=subprocess.PIPE, text=True)
	# Run the second command (cut -d ' ' -f 1) using the output of the first command
	cutSysctl = subprocess.Popen(['cut', '-d', ' ', '-f', '1-3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	#output
	#Use communicate to get input of command Sysctl with addition Cutsysctl
	#We then encode this output to bytes to avoid str has no attr fileno, as we expect a byte reply
	#Use _ to avoid returning tuple with error, just string output
	output, _ = cutSysctl.communicate(input=grabSysctl.stdout.encode())

	#Decode our byte data to reg utf-8 string text
	#splitlines to get easy output to produce list
	if output:
		#Decode such params we got from befores sub process commands into utf-8
		parameters = output.decode('utf-8')

		for x in parameters.splitlines():
			if "=" in x:
				#print(f"CURRENT PARAM BEING TESTED : {x} \n")
				#split the FIRST = within tuple / keypairs
				currentVal, currentKey = x.split(" = ", 1) 
			
				#Don't bother with kernal params = NONE
				if currentKey != None or "NONE":
					##We now can put currentVal with key pair currentKey in new Dictioanry
					#Instead of append, we simply use the '=' to instead put values together in each indicie
					#Ex output:    net.iv4.log.martians : 0
					currentParams[currentVal.strip().lower()] = currentKey.strip()

				#print(f"Checking parameter: {x}")
						
			
		
		
	return currentParams


def correct():
	okparams = []
	c = 0
	pxt = getParams()

	for key, val in PARAMS:
		#use .get to grab val associated with pair
		checkKey = pxt.get(key.lower())
		if checkKey:
			if checkKey != val:
				print(f"The value for {key} does not match the key for secure params: Current: {checkKey} Wanted: {val}")
				time.sleep(0.8)
			else:
				print(f" The value {val} for key: {key} is okay!")
				okparams.append(key)
				c += 1
				time.sleep(1.2)

	print(f"\n\n Unchanged Keys: {str(okparams)}")




#Function to actually harden specific systemd service files
def hardenCaps():
	#For all unitpaths -- systemd-analyze unit-paths
	#Check specific config file of service just edited:
	#sudo systemd-analyze verify /lib/systemd/system/chrony.service



	




	pass





def main():
	who = whoami()
	whats = whatsmyos()
	if who:
		if whats:
			print(correct())
	else:
		sys.exit("Please run script with sudo or root privledges")

if __name__ == "__main__":
	main()
