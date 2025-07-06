#!/bin/bash


#Find local processes ran via user
read -p "Process Name (Ex: Firefox): " proc
x=$(whoami)
pidofthing=$(ps -u "$x" | grep "$proc" | cut -d ' ' -f 4)
if [ -z "$pidofthing" ]; then
	sleep 1 
	"No Output for a PID or process found..."
	exit 0

else
	echo -n "YOUR APPS PID:" && ps -u "$x" | grep "$proc" | cut -d ' ' -f 4
	read -p "Enter pid here: " pid
	echo "YOUR BINARIES RUN LOCATION:"
	ls -l /proc/"$pid"/exe
fi
