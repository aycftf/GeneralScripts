#!/usr/bin/env bash
#Script by whftf, auditd framework by ....

#Script For ausearch, auditctl and the audit suite! For Logging specific tasks
#And Directories within Directories


cat << EOF

⠤⠤⠤⠤⠤⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠶⠶⠶⠦⠤⠤⠤⠤⠤⢤⣤⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠄⢂⣠⣭⣭⣕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉
⠀⠀⢀⠜⣳⣾⡿⠛⣿⣿⣿⣦⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣍⣀⣦⠦⠄⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣄⣽⣿⠋⠀⡰⢿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠛⠛⡿⠿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣁⣂⣤⡄⠀⠀⠀⠀⠀⠀
⢳⣶⣼⣿⠃⠀⢀⠧⠤⢜⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⡇⠀⣀⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠁⠐⠀⣀⠀⠀
⠀⠙⠻⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⡝⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠠⠃⠁⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠋⠀⠀
⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⢸⣿⣿⡃⢼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡏⠉⠉⠻⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠀⠀⠰⡒⠊⠻⠿⠋⠐⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣇⡀⠀⠑⢄⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠠⠤⠤⠔⠙⠻⠿⠋⠱⡑⢄⠀⢠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠻⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⡵⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⣀⠀⠀⠀⠀⠀⢀⣤⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⠛⠓⠒⠲⠿⢍⡀⠀⠀⠀⠀⠀⠀

EOF



checkroot=$(echo "$UID")
if [ "$checkroot" -ne 0 ]; then
	echo "please run as root" && exit 1
fi



##### EASY TODO: Implement logrotate feature to auto dump config for user


PROC=$(ps -ef | grep audit.sh | grep -v grep | awk '{print $2}')
echo -e "Current processes: $procs "
dirr=$(pwd)
scriptDir=$(file "$dirr"/audit.py)
deps() {
	if [[ -z "$scriptDir" ]]; then
		echo -e "Repo for automation script not found...."
	fi
	##Check for runtime / service enabled for systemctl
	systemctl list-units --type=service --state=running | grep -q -e "auditd.service" -e "Audit Logging Service"
	#Check status of grep
	running=$?
	systemctl --runtime status | grep -q auditd.service
	runtime=$?
	
	if [[ "$running" -eq 0 && "$runtime" -eq 0 ]]; then
        	echo -e "Auditd services started on boot as well as started...."
	else
        	echo -e "Restarting service and potentially adding it to boot now" && sleep 1

		#Simple enable the service
		systemctl enable auditd.service 

	fi



}





deps
echo -e "Current KeyWords for audit file:"
auditctl -l | awk '{print $6}'
echo -e "\n"
sleep 1


current_amount_of_rules=$(wc /etc/audit/audit.rules|awk '{print $2}')
#Show general auditctl info
##Delete rules ######Careful with this

if  (( "$current_amount_of_rules" > 6 )); then
	read -p "Delete Current auditctl rules? (y/n) " -en 1 deleteme
	if [[ "$deleteme" =~ y|Y || -z "$deleteme" ]]; then
		auditctl -D
		echo -e "Refreshed the current rules..."


	else


		echo -e "\n\n Keeping related rules..." && cat /etc/audit/audit.rules
	fi


fi 

echo -e "Current auditd configuration: \n"
auditctl -s
sleep 0.5
echo -e "Live Log Command and Location: sudo tail -f /var/log/audit/audit.log"
echo -e "Extra Live Log Command and Location: sudo tail -f /var/log/messages & journalctl -f --system"
sleep 0.5
if file loop.txt > /dev/null 2>&1; then
	rm loop.txt > /dev/null 2>&1;
fi



read -p "Create Any rule specific to a directory? (y/n): " -en 1 create

if [[ "$create" =~ "y"|"Y" ]]; then 
	while true; do
	read -p "Specify the Directory to watch over here: (Ex: /home/user/Documents) " dir
	read -p "Specify the KeyWord used to search up the audit log for this directory here: " name


	#Check for valid directory input (No more then one / and string)
	#E.G.:  //home -- incorrect     /home --- correct
	if ! [[ "$name" =~ "//"+ ]]; then

		if auditctl -w "$dir" -p rwa -k "$name"; then
		echo -e "Rule imported correctly! \n\n\n"
		echo "Imported keyword and rule name "$name" with directory "$dir" "
		sleep 1

		else
			
			read -p  "Error with importing rule.... try again? (y/n): " -en 1 tryagainone
			if [ "$tryagainone" =~ y|Y ]; then 
			
				echo -e "Thisis why"
			else
				echo -e "Current Rules: $(sudo auditctl -l) " 

			fi



		fi
		sleep 1 && echo -e "\n\n\n"
		auditctl -l | grep "$name"

	else

		echo -e "Please enter valid directory path..."
		continue


	fi

	read -p "Continue Adding more Rules/Directories? (y/n): " -en 1 continue

	if [ "$continue" == "y" ]; then 
		echo "Creating Another Rule...."
		continue

	else


		break
	fi

	done


else
	echo "Skipping...."
	sleep 1

fi


#Implement date feature later to check only from specific dates ... 

auditbin=$(which auditctl)
#Put all specific auditkeywords in a temp file
"$auditbin" -l | awk '{print $6}' >> loop.txt



##CORE UTILS AND RULES SOURCED FROM: https://github.com/Neo23x0/auditd/blob/master/audit.rules
RULELOKO="/etc/audit/rules.d/audit.rules"
TEMPUT="$(pwd)/auditnew.rules"
read -p "OPTIONAL... Create new auditd audit.rules to go by? USES Neo23x0 auditd.rules and other custom ones such as tuning down noise; (y/n) " -en 1 addNeo 
#Move to newline after input
echo
if [[ "$addNeo" =~ y|Y ]]; then
	echo -e "Generating core audit.rules file..."
	touch "$TEMPUT"


	cat <<EOF >> "$TEMPUT"
## Increase the buffers to survive stress events.
## Make this bigger for busy systems
-b 8192

## This determine how long to wait in burst of events
--backlog_wait_time 60000

## Set failure mode to syslog
-f 1

##Attempt to ignore execve syscall from Auditd when writing rules
-w /etc/sysctl.conf -p wa -k sysctl
-w /etc/sysctl.d -p wa -k sysctl
## Stunnel
-w /usr/sbin/stunnel -p x -k stunnel
-w /usr/bin/stunnel -p x -k stunnel
## Cron configuration & scheduled jobs
-w /etc/cron.allow -p wa -k cron
-w /etc/cron.deny -p wa -k cron
-w /etc/cron.d/ -p wa -k cron
-w /etc/cron.daily/ -p wa -k cron
-w /etc/cron.hourly/ -p wa -k cron
-w /etc/cron.monthly/ -p wa -k cron
-w /etc/cron.weekly/ -p wa -k cron
-w /etc/crontab -p wa -k cron
-w /var/spool/cron/ -p wa -k cron
## Added to catch netcat on Ubuntu
-w /bin/nc.openbsd -p x -k susp_activity
-w /bin/nc.traditional -p x -k susp_activity
## Sbin suspicious activity
-w /sbin/iptables -p x -k sbin_susp
-w /sbin/ip6tables -p x -k sbin_susp
-w /sbin/ifconfig -p x -k sbin_susp
-w /usr/sbin/arptables -p x -k sbin_susp
-w /usr/sbin/ebtables -p x -k sbin_susp
-w /sbin/xtables-nft-multi -p x -k sbin_susp
-w /usr/sbin/nft -p x -k sbin_susp
-w /usr/sbin/tcpdump -p x -k sbin_susp
-w /usr/sbin/traceroute -p x -k sbin_susp
-w /usr/sbin/ufw -p x -k sbin_susp
## Suspicious shells
-w /bin/ash -p x -k susp_shell
-w /bin/csh -p x -k susp_shell
-w /bin/fish -p x -k susp_shell
-w /bin/tcsh -p x -k susp_shell
-w /bin/tclsh -p x -k susp_shell
-w /bin/xonsh -p x -k susp_shell
-w /usr/local/bin/xonsh -p x -k susp_shell
-w /bin/open -p x -k susp_shell
-w /bin/rbash -p x -k susp_shell
## Pam configuration
-w /etc/pam.d/ -p wa -k pam
-w /etc/security/limits.conf -p wa  -k pam
-w /etc/security/limits.d -p wa  -k pam
-w /etc/security/pam_env.conf -p wa -k pam
-w /etc/security/namespace.conf -p wa -k pam
-w /etc/security/namespace.d -p wa -k pam
-w /etc/security/namespace.init -p wa -k pam
##SysCall Rules!
-a always,exit -F arch=b64 -F exe!=/usr/sbin/auditctl -S chmod -k chown_monitor
-a always,exit -F arch=b64 -F exe!=/usr/sbin/auditctl -S chown -k chmod_monitor
-a always,exit -F arch=b64 -F exe!=/usr/sbin/auditctl -S umask -k umaskcheck
-a always,exit -F arch=b64 -F exe!=/usr/sbin/auditctl -S connect -k connects
-a always,exit -F arch=b64 -S accept -k accepts
-a always,exit -F arch=b64 -S open -perm=w -k writeattempts
-a always,exit -F arch=b64 -S creat -k createfile
-a always,exit -F arch=b64 -S mount -S umount2 -F auid!=-1 -k mount
-a always,exit -F arch=b64 -S mknod -S mknodat -k specialfiles
-a always,exit -F arch=b64 -S sethostname -S setdomainname -k network_modifications
-a always,exit -F arch=b64 -S 44 -F a2=16 -F success=1 -F key=network_connect_4
-a always,exit -F arch=b64 -F euid=0 -F auid>=1000 -F auid!=-1 -S execve -k rootcmd
-a always,exit -F arch=b64 -S rmdir -S unlink -S unlinkat -S rename -S renameat -F auid>=1000 -F auid!=-1 -k delete

EOF
echo
	sleep 4
	cat /etc/audit/rules.d/audit.rules | grep -v "#" |  awk '{print $6}' | uniq >> loop.txt
	echo -e "Generating backup of current audit.rules"
	if scp /etc/audit/rules.d/audit.rules /etc/audit/rules.d/auditrules"$(date)".BAK; then
		ls -lah auditnew.rules && cat auditnew.rules
		mv auditnew.rules /etc/audit/rules.d/audit.rules && systemctl restart auditd 
		echo -e "\n\n" && sleep 1
		echo -e "New Default Rules: " && auditctl -l


	else
		echo -e "Copying of file to auditd directory failed... checck directory permissions: "
		stat /etc/audit

	fi

else
	echo -e "Skipping..." && sleep 1

fi


#Generic strings to check against ausearch
gen=(

	avc
	ANOM_ADD_ACCT 
	ANOM_MOD_ACCT 
	ANOM_LOGIN_FAILURES
	CRED_DISP
	USER_END
	BPF
	NETFILTER_CFG
	USER_AVC
)



if python3 audit.py; then


	user=$(whoami)
	#Loop thru indicies 
	for genn in "${gen[@]}"; do
		echo -e "Searching Keyword "$genn" now... \n\n\n"
		sleep 1
		#Reference each keyword with ausearch framework
		checkme=$(sudo ausearch -m "$genn" --start today)

		echo "$checkme" >> genaudit.txt 
		if ! ls -l genaudit.txt| awk '{print $1}' | grep -q ".rw-r-----."; then
			sudo chown -R "$user":"$user" genaudit.txt && sudo chmod 640 genaudit.txt
		
		fi
		echo -e "Nothing found for "$genn"... Good Sign"
		

		sleep 1
		echo -e "\n\n\n\n"
	

	done

	#Check for all syscalls
	ausearch -m execve --start today


	##Check for recent network connections produced via cli:
	ausearch -k network_connect_4 | grep -v snapd | grep -v ssh | grep -v auditctl | grep "comm"
	#exit


fi

#Show small human readable summary of events 
sudo aureport --summary
sudo aureport --avc
sudo aureport --auth  
sudo aureport --anomaly
sudo aureport --virt

dir=$(pwd)
rm "$dir"/loop.txt


read -p "Clean all procs? " procs

if [[ "$procs" =~ y|Y ]]; then
	"$PROC" | xargs kill -9
fi
