#!/bin/bash

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


PROC=$(ps -ef | grep audit.sh | grep -v grep | awk '{print $2}')

echo -e "Current processes: $procs "

dirr=$(pwd)
scriptDir=$("$dirr"/audit.py)
deps() {


	if [[ -z "$scriptDir" ]]; then
		echo -e "Repo for automation script not found...."
	fi

	##Check for runtime / service enabled for systemctl
	sudo systemctl list-units --type=service --state=running | grep -q -e "auditd.service" -e "Audit Logging Service"
	#Check status of grep
	running=$?
	sudo systemctl --runtime status | grep -q auditd.service
	runtime=$?

	
	if [[ "$running" -eq 0 && "$runtime" -eq 0 ]]; then
        	echo -e "Auditd services started on boot as well as started...."
	else
        	echo -e "Restarting service and potentially adding it to boot now" && sleep 3

		#Simple enable the service
		sudo systemctl enable auditd.service 

	fi



}





deps
echo -e "\n Current KeyWords for audit file: \n "
echo -e "\n\n\n"
sudo auditctl -l | cut -d ' ' -f 6
echo -e "\n\n\n"
sleep 3
clear


current_amount_of_rules=$(sudo wc /etc/audit/audit.rules|cut -f2 -d ' ')
#Show general auditctl info
##Delete rules ######Careful with this

if  [ "$current_amount_of_rules" > 6 ]; then
	read -p "Delete Current auditctl rules? (y/n) " -en 1 deleteme
	if [[ "$deleteme" =~ y|Y || -z "$deleteme" ]]; then
		sudo auditctl -D
		echo -e "Refreshed the current rules..."


	else


		echo -e "\n\n Keeping related rules..." && sudo cat /etc/audit/audit.rules
	fi


fi 


#Delete and show params anyways if wc below 6 (Default startup wc)
sudo auditctl -s
sudo auditctl -D


sleep 2
echo -e "\n Live Log Command and Location: sudo tail -f /var/log/audit/audit.log \n "
echo -e "\n Live Log Command and Location: sudo tail -f /var/log/messages"
sleep 2
rm loop.txt



read -p "Create Any rule specific to a directory? (y/n): " create

if [[ "$create" =~ "y"|"Y" ]]; then 
	while true; do
	read -p "Specify the Directory to watch over here: (Ex: /home/user/Documents) " dir
	read -p "Specify the KeyWord used to search up the audit log for this directory here: " name


	#Check for valid directory input (No more then one / and string)
	#E.G.:  //home -- incorrect     /home --- correct
	if ! [[ "$name" =~ "//"+ ]]; then

		sudo auditctl -w "$dir" -p rwa -k "$name"
		sleep 1 && echo -e "\n\n\n"
		sudo auditctl -l | grep "$name"

	else

		echo -e "Please enter valid directory path..."
		continue


	fi


		#Check if executedcorrectly w/ exit status $?
	if [ $? -eq 0 ]; then
		echo -e "Rule imported correctly! \n\n\n"
		echo "Imported keyword and rule name "$name" with directory "$dir" "
		sleep 1
		
	else
		echo -e "\n Error with audit creation, try again!"
		continue
	fi
	
	read -p "Continue Adding more Rules/Directories? (y/n): " continue

	if [ "$continue" == "y" ]; then 
		echo "Creating Another Rule...."
		continue

	else

		break
	fi

	done


else
	echo "Skipping...."
	sleep 2

fi


#Implement date feature later to check only from specific dates ... 

#Put all specific auditkeywords in a temp file
sudo auditctl -l | cut -d ' ' -f 6 >> loop.txt

#Generic strings to check against ausearch
gen=(

	avc
	ANOM_ADD_ACCT 
	ANOM_MOD_ACCT 
	ANOM_LOGIN_FAILURES
	chmod_monitor
	umaskcheck
	connects
	accepts
	writeattempts
	createfile
	chown_monitor
)


if python3 audit.py; then




	echo -e "Checking generic ausearch IOC indicators...."
	sudo auditctl -a exit,always -F arch=b64 -S chmod -k chown_monitor
	sudo auditctl -a exit,always -F arch=b64 -S chown -k chmod_monitor
	sudo auditctl -a exit,always -F arch=b64 -S umask -k umaskcheck 
	sudo auditctl -a exit,always -F arch=b64 -S connect -k connects
	sudo auditctl -a exit,always -F arch=b64 -S accept -k accepts
	sudo auditctl -a exit,always -F arch=b64 -S open -perm=w -k writeattempts
	sudo auditctl -a exit,always -F arch=b64 -S creat -k createfile 


	user=$(whoami)
	#Loop thru indicies 
	for genn in "${gen[@]}"; do
		echo -e "Searching Keyword "$genn" now... \n\n\n"
		sleep 2
		checkme=$(sudo ausearch -m "$genn" --start today)

		echo "$checkme" >> genaudit.txt 
		if ! ls -l genaudit.txt| cut -f1 -d ' ' | grep -q ".rw-r-----."; then
			sudo chown -R "$user":"$user" genaudit.txt && sudo chmod 640 genaudit.txt
		
		fi
		echo -e "Nothing found for "$genn"... Good Sign"
		

		sleep 3
		echo -e "\n\n\n\n"
	

	done

	#Check for generic syscall infofi
	sudo ausearch -m execve --start today

	#exit


fi

#Show small human readable summary of events 
sudo aureport --summary
sudo aureport --avc
sudo aureport --auth  
sudo aureport --anomaly
sudo aureport --virt

dir=$(pwd)
echo -e "$dir"
findfiles =$((find "$dir"/loop.txt -type f && find "$dir"/genaudit.txt type -f -perms 640))

if "$findfiles"; then
	rm "$dir"/loop.txt #&& sudo rm "$dir"/genaudit.txt

fi


read -p "Clean all procs? " procs

if [[ "$procs" =~ y|Y ]]; then
	"$PROC" | xargs kill -9
fi
