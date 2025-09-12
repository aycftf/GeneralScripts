#!/usr/bin/env bash

#Pull all user services


ray=$(cat userservs.txt)
whoam=$(whoami)
findme=$(find /home/"$whoam"/ -type f -name "userservs.txt" )
stderrr=$(echo "$?")
#check for non empty var with -n
if [ -n "$findme" ]; then
	echo -e "\n $findme \n"
	read -p "Correct file? (y/n): " -en 1 delfile


	if [[ "$delfile" =~ y|Y ]]; then

		rm "$findme"
		sleep 2 && echo -e "\n\n\n"

	fi
fi

sudo ps aux | grep -v "grep" | grep -v "^root" | awk 'NR>1 {print $11,$2}' | xargs -n1 basename >> userservs.txt
sudo chown -R "$whoam":"$whoam" userservs.txt && sudo chmod ug+rw userservs.txt
#Read from line one then line two to compare
while IFS= read -r command && IFS= read -r pid; do
	if [ -z "$pid" ]; then
		continue
	fi
	echo -e "\n Capabilities of process: $command "
	if getpcaps "$pid" && sleep 0.5s; then
		echo ""
	else
		echo "No pid with "$command" "
	fi
done < userservs.txt

