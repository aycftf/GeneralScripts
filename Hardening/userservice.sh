#!/usr/bin/env bash

#Pull all user services
ray=$(cat userservs.txt)
whoam=$(whoami)
stderrr=$(echo "$?")
sudo ps aux | grep -v "grep" | grep -v "^root" | awk 'NR>1 {print $11,$2}' | xargs -n1 basename >> userservs.txt
while IFS= read -r command && IFS= read -r pid; do

	if [ -z "$pid" ]; then
		continue
	fi
	echo -e "\n Capabilities of process: $command "
	if getpcaps "$pid" && sleep 2; then
		echo ""
	else
		echo "No pid with "$command" "
	fi
done < userservs.txt

