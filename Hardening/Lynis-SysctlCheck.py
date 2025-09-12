import os
import sys
import subprocess
import sys
import re
import time


#Script for sysctl Hardening Parameters and Kernal Hardening

#Documentation Surrounding different Kernal/Sysctl Params Regarding argument level / rule level:

#https://linux-audit.com/kernel/sysctl/kernel/
#Lynis audit system
#sudo systctl -A


IP4_PARAMS = { 
	'net.ipv4.conf.default.accept_redirects' : "0", 
	'net.inet.ip.linklocal.in.allowbadttl' : "0", 
	'net.ipv4.ip_forward' : "0", 
	'net.ipv4.conf.all.accept_source_route' : "0", 
	'net.ipv4.conf.all.secure_redirects' : "0", 
	'net.ipv4.conf.all.log_martians' : "0", 
	'net.ipv4.conf.default.log_martians' : "0", 
	'net.ipv4.icmp_echo_ignore_broadcasts' : "0", 
	'net.ipv4.icmp_ignore_bogus_error_responses' : "0", 
	'net.ipv4.tcp_syncookies' : 0, 
	'net.ipv4.conf.all.send_redirects' : 0, 
	'net.ipv4.conf.default.send_redirects' : 0}
IP6_PARAMS = { 'net.ipv6.conf.all.disable_ipv6', 'net.ipv6.conf.all.addr_gen_mode', 'net.ipv6.conf.all.autoconf', 'net.ipv6.conf.all.forwarding', 'net.ipv6.conf.all.accept_dad', 'net.ipv6.conf.all.accept_ra', 'net.ipv6.conf.all.accept_ra_from_local', 'net.ipv6.conf.all.accept_untracked_na ' }
KERNAL_PARAMS ={  
	'kernel.yama.ptrace_scope', 
	'fs.protected_fifos', 
	'fs.protected_hardlinks',
	 'fs.protected_regular', 
	 'fs.protected_symlinks', 
	 'fs.suid_dumpable', 
	 'kernel.core_uses_pid', 
	 'kernel.apparmor_restrict_unprivileged_unconfined'}

REMOVE_TRAILING_NUMS = r'\d+'

def check(value):

	ifExist = None

	##Conditional to test if sysctl parameter exists on system
	try:
		ifExist = subprocess.run(['sysctl', value], check=False, text=True, capture_output=True)

		if "permission denied: " in ifExist.stderr:
			print("Missing perms")
			return None

	except subprocess.CalledProcessError:
		print(f"param: {value} Not Found In System!")
	except Exception as pt:
		print(f"unexpected error: {pt}")
		return None
	
	return ifExist


	




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
				if check(currentVal) and currentKey != None or "NONE":
					##We now can put currentVal with key pair currentKey in new Dictioanry
					#Instead of append, we simply use the '=' to instead put values together in each indicie
					#Ex output:    net.iv4.log.martians : 0
					currentParams[currentVal.strip().lower()] = currentKey.strip()

				#print(f"Checking parameter: {x}")
						
			
		
		
	return currentParams


def correct():
	c = 0
	pxt = getParams()
	for key, val in IP4_PARAMS.items():
		#use .get to grab val associated with pair
		checkKey = pxt.get(key.lower())
		if checkKey:
			if checkKey != val:
				print(f"The value for {key} does not match the key for secure params: Current: {checkKey} Wanted: {val}")
				time.sleep(0.8)
			else:
				print(f" The value for {key} and {val} for key are okay!")
				c += 1

	print(f"Unchanged Keys: {c}")

def main():
	print(correct())

if __name__ == "__main__":
	main()
