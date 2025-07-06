#!/bin/bash
##Only run such check in interactive tty

##Grab term session
if [ -t 0 ] ; then
	stdbuf -oL -eL doas dnf5 update 2>&1 |
	while CHECK= read -r line; do

        	if [[ "$line" == *"incorrect password"* || "$line" == *"doas: Authentication failed"* ]]; then
                	echo "BAD PASSWORD DETECTED"
			sudo shutdown now
       		elif [[ "$line" == *"Updating and loading repositories:"* || "$line"  == *"Nothing to do."* ]]; then
                	echo "Correct Password!"
			sudo getent group | grep wheel

        	else

            		echo "Your'e Good!"
			sudo getent group | grep wheel
                	exit 0
        	fi
	done
fi
