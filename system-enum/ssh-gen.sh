##Show newly configured iptables



#!/usr/bin/bash

sudo iptables -L -v -n




#Block ip using iptables
while true; do
    read -p "Drop specific ip? (y/n) " block
    
    if [ "$block" = "y" ]; then
        read -p "Enter IP to block: " IP
        sudo iptables -t filter -A OUTPUT -d "$IP" -j DROP
        sudo iptables -t filter -A FORWARD -d "$IP" -j DROP
        sudo iptables -t filter -A INPUT -d "$IP" -j DROP
	##log fix for future log from input mac source output via sus ip
	##sudo iptables -A INPUT -i "$mac" -j LOG --log-prefix "SUSPICIOUS IP: " --log-level 7
        break
    elif [ "$block" = "n" ] || [ -z "$block" ]; then
        echo ""
        break
    else
        echo "Incorrect Input..."
    fi
done




while true; do
    read -p "Add ssh connection? (Options: y/n) " sshorno 
    if [ -z "$sshorno" ]; then
        echo -e "\n"
        echo "Must be valid input..."
        echo "Try again"
        continue
    elif [ "$sshorno" = "y" ]; then
        read -p "Enter ip of machine to allow ssh throughput: " sshcon
        read -p "Enter the machine name or username you're connecting thru: " sshname
	read -p "Enter Port To connect ssh to (e.g. 22) " porty
        if [ -z "$sshcon" ]; then
            echo "Incorrect input.... skipping sequence"
            break
        fi

        echo "Adding now...."
        echo -e "\n"
        ##Add ssh rules via sshcon ip
        sudo iptables -A INPUT -m state --state NEW,ESTABLISHED,RELATED --source "$sshcon" -p tcp --dport 22 -j ACCEPT
        sudo iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED --source "$sshcon" -p tcp --sport 22 -j ACCEPT
        sudo iptables -L -v -n | grep "22"
        sleep 1
        read -p "Gen Keys? (y/n) " sshkeys

        if [ "$sshkeys" = "y" ] || [ "$sshkeys" = "yes" ]; then
            read -p "Enter the directory to generate ssh keys.. (Default Location AND keyname If Nothing Entered: ~/.ssh/keysatfirst/NEWCREATEDKEY!): " sshkeysdir
            echo "Generating strong key pairs now..."
            sleep 1
            if [ -z "$sshkeysdir" ]; then
                sshkeysdir="$HOME/.ssh/keysatfirst/NEWCREATEDKEY"
            fi
            sudo rm -rf ~/.ssh/keysatfirst/*
            sudo ssh-keygen -t ed25519 -a 1000 -f "$sshkeysdir"
            sudo ls ~/.ssh/keysatfirst/

            sleep 1
            echo \n
            echo "Copying keys over to other end user $sshcon user now...."
            echo \n
            echo "Other user must have sshd running or ssh server running..."
            echo \n
            sleep 1

            # Execute ssh-copy-id command and store result
            if sudo ssh-copy-id -p "$porty" -i "${sshkeysdir}".pub "${sshname}@${sshcon}"; then
                echo "Successfully copied SSH key to remote host"
                echo "SSH INTO YOUR BOX WITH YOUR KEY COMMAND: sudo ssh -i ${HOME}/${sshkeysdir} -p ${porty}  ${sshname}@${sshcon}"
                echo "SCP INTO YOUR BOX WITH YOUR KEY COMMAND: sudo scp -i ${HOME}/${sshkeysdir} -P 23 ${sshname}@${sshcon}:<filepath_on_host> <path_on_client>"
                sleep 2
                break
            else
                echo "Failed to copy SSH key to remote host. Please check if:"
                echo "- The remote host is reachable"
                echo "- SSH server is running on remote host" 
                echo "- You have the correct username and permissions"
                sleep 1
                break
            fi

            sleep 1

        fi
        break
    elif [ "$sshorno" = "n" ]; then
        echo ""
        echo "Continuing on with script...."
        break
    else
        echo "Invalid input. Please enter y or n."
        continue
    fi
done






