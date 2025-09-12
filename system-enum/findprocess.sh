#!/usr/bin/env bash


#Find local processes ran via user
read -p "Process Name (Ex: Firefox): " proc
x=$(whoami)
pidofthing=$(ps -u "$x" | grep "$proc" | awk 'NF=1 {print $1}')
if [ -z "$pidofthing" ]; then
	sleep 1 
	"No Output for a PID or process found..."
	exit 0

else
	loco=$(ls -l /proc/"$pidofthing"/exe | cut -d ' ' -f11)
	if [ -n "$loco" ]; then

		echo "YOUR BINARIES RUN LOCATION: "$loco" "
		#Check functions embedded within binary
		echo -e "Functions within $loco : \n "
		strings "$loco" | grep -E '^[a-z0-9_]{4,32}\(\)' | awk '{print $1}' | sort | uniq
	fi
	echo -e "YOUR BINARIES PID ON THE SYSTEM: \n $pidofthing"
	echo -e "Capabilities your process utilizes if any... "
	getpcaps "$pidofthing" && sleep 2
	exit 0 
fi



