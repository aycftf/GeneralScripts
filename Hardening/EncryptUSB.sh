#!/usr/bin/env bash


#Credit
#For loop a-z: https://askubuntu.com/questions/873314/for-loop-with-alphabet

##TODO / Things we need to figure out:
#TODO: Add more mount options 2 scan?
#A) How to run cryptsetup skipping info questioanre
#B) How to cleanly get disk / usb size and partition auto for user
#C) Cryptsetup commands

##$x = partition sd_ found via usb mount
findmount=$(mount | cut -d ' ' -f1-3 | grep "/dev/sd$x")
dirrn=$(pwd)
verbose=0
ERRORECHO=$(echo $?)
BOLD='\e[1m'
RESET='\e[0m'
GREEN='\e[034m' # red
RED='\e[032m'
YELLOW='\e[033m'
BOLDYELLOW="$BOLD""$YELLOW"
BOLDRED="$BOLD""$RED"
BLUE='\e[034m' #blue
BOLDGREEN="$BOLD""$GREEN"
BOLDBLUE="$BOLD""$BLUE"
#\033]00m\]   # white
#033]01;36\] # bold green
#\033]02;36\] # green
#\033]01;34\] # blue
#\033]01;33\] # bold yellow




helpfunc() {
	clear
	echo -e "$BOLDGREEN"

	cat << EOF



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣷⢸⣿⣿⡜⢯⣷⡌⡻⣿⣿⣿⣆⢈⠻⠿⢿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⢳⣿⣿⣿⣿⣿⣿⡜⣿⣿⣧⢀⢻⣷⠰⠈⢿⣿⣿⣧⢣⠉⠑⠪⢙⠿⠿⠿⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣱⡇⡞⣿⣿⣿⣿⣿⣿⡇⣿⣿⡏⡄⣧⠹⡇⠧⠈⢻⣿⣿⡇⢧⢢⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⢃⢿⣿⣿⣿⣿⣿⣷⣿⣿⠇⢃⣡⣤⡹⠐⣿⣀⢻⣿⣿⢸⡎⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⣿⣿⠘⡸⣿⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⢟⡷⠈⠋⠃⠎⢿⣿⡏⣿⠀⠘⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢹⣿⣿⡐⢡⢹⣿⣿⣿⣿⡏⣿⢣⣿⣿⡑⠁⠔⠀⠉⠉⠢⡘⣿⡇⣿⡇⠀⡀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⣿⣿⣇⠇⢣⢻⣿⣿⣿⡇⢇⣾⣿⣿⡆⢸⣤⡀⠚⢂⠀⢡⢿⡇⣿⡇⠀⢿⠀⠀⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠠⠹⣿⣿⡘⣆⢣⠻⣿⣿⢈⣾⣿⣿⣿⣶⣸⣏⢀⣬⣋⡼⣠⢸⢹⣿⡇⢠⣼⠙⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠁⠹⣿⣇⠹⡃⠃⠙⡇⠘⢿⣿⣿⣿⣿⣿⣏⣓⣉⣭⣴⣿⠘⢸⣿⠁⠘⠋⠀⠹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠈⢿⣇⠂⣷⠄⠐⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⢸⡏⠀⢀⣠⣴⣾⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠙⠆⠈⠢⠲⠥⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣸⠁⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠃⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡏⠹⣿⣿⡿⠫⠊⠀⠀⠀⣶⠀⢻⣿⣿⣿⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⢋⠀⠀⠀⠀⢀⣼⣿⡆⠈⣿⣿⣿⡟⣱⡷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣁⡀⠨⣛⠿⠶⠄⢀⣠⣾⣿⣿⣷⠀⢹⣿⡟⣴⠈⢃⣶⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⡿⠀⡀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠻⣿⣿⢀⠙⠻⠿⣿⣿⣿⣿⣿⣿⡇⠁⣿⠟⡀⠈⣧⢰⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠴⠮⣥⠻⢧⣤⣄⣀⡉⢩⣭⣍⣃⣀⣩⠎⢀⣼⠉⣼⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠁⣛⠓⢒⣒⣢⡭⢁⡈⠿⠿⠟⠹⠛⠁⠀⠀⠀⠰⠃⠂⠀⠀⠀

script by whftf:)

EOF

	sleep 2.1
	clear
	
	echo -e "$RESET" && echo  -e "$BOLDRED"
	echo -e " COMMAND HELP! "
	echo -e "$BOLDRED" && echo -e " [*] "$pwd"/EncrpytUsb.sh -f --- Finding Usb's currently mounted on your system.. "
	echo -e " [*] This is a pre-requisite to encrypting your usb\n"
	echo -e " [*] "$pwd"/EncryptUsb.sh -f allows for "$BLDYELLOW" THREE "RESET" "BOLDRED" different methods to wipe usb data before encrypting! "
	echo -e " \n\n "
	echo -e " [*] DataWipe Method #1) Quickest, simply uses dd to overwrite data with low amounts of block chunks and less random entropy. "
	echo -e " [*] DataWipe Method #2) Slower, but ideal. Wipe external drive (No SSDS!) with a superior method then standard dd, and an ample amount of random generated data! "
	echo -e " [*] DataWipe Method #3) Slowest! Overwrite external usb with incredible amount of random data, utilizing both secure methods! "
 


	echo -e "$RESET"


}

deps() {

	#checkcrypt=$(which cryptsetup && cryptsetup --version  < /dev/null 2>&1)
	#sudo apt-get update -y && sudo apt-get upgrade -y --show-progress 
	DEPS=(cryptsetup openssl wipefs shred fdisk dd)
		
		echo -e "$BOLDYELLOW"


		for xx in "${DEPS[@]}"; do

			if which "$xx" 2>&1 > /dev/null; then
				echo -e "$xx Installed! "
				sleep 1.4
				continue
			else
				echo -e "Error. Must Download "$xx" " && sleep 1
				exit 2


			fi
		done		 
		


		echo "deps satisfied.."
		echo -e "$RESET"

}



wipe() {

	errors=$(echo $?)

	if [ "$OPTARG" == "fast" ]; then

		
		echo -e "Quickly Wiping Data with dd... \n"
		sleep 2
		echo -e "Works!"
		actualdisk=$(sudo fdisk -l | grep "/dev/sd" | grep -v "Disk" | cut -f 1 -d ' ')

		lsblk && echo -e "\n"
		sleep 1

		read -p "Is "$actualdisk" the correct usb mount location? " -en 1 correctmount
		if [[ "$correctmount" =~ y|Y ]]; then

			#Unmount usb firstly

			sudo umount "$actualdisk"
			#Wipe usb second
			sudo wipefs -a --force "$actualdisk"

			if [ "$errors" == 0 ]; then

				sudo dd if=/dev/zero of="$actualdisk" bs=1M status=progress && exit 0



			#Secure: shred -v -z --iterations=2 $DEVICE
			#slow: dd bs=512 count=4 if=/dev/random of=$DEST iflag=fullblock
			#slow: sudo dd if=/dev/urandom of=/dev/sdX bs=1M status=progress
			fi





		fi


		exit 0
		

	fi

}


findusb() {



	if deps; then

		echo -e "Finding usb on system..."
		echo -e "Making sure usb is mounted..."

		#Loop thru all possible letters for mapping
		alph=(a b c d e f g h i j k l m n o p q r s t u v w x y z)
	


		#loop thru indicies of alph
		#Avoid stderr + stdout output
		for x in "${alph[@]}"; do
			
			if sudo mount | cut -f1 -d ' ' | grep /dev/sda | grep -v "grep" > /dev/null 2>&1; then
				sleep 1
				echo -e   " \n [*] Usb Found At: /dev/sd$x "
				echo -e " \n [*] Usb Mounted.... Continuing Process.. "
				sleep 2




				if echo -e " USB mounted at: $findmount"; then


					read -p "Wipe Drive Before Encrpytion? (Recommended For Security, enter y/n + fast/secure for how fast to wipe a drive... e.g: y fast): " -en 9 wipeyesorno fastorsecure


					if [[ "$wipeyesorno" =~ y|Y ]]; then
						#Ubutnu tested only via cut / media mount
						echo -e "Now wiping drive.."

						./EncryptUSB.sh -w fast

					else
						echo -e "skipping wiping process... "
						break

					fi

				else
				
					exit 1	
				fi

				exit 0
	 
			else
				continue

			fi


		done



		echo -e "Cannot find mount.... Re plug in usb or check lsusb for driver check " && lsusb
		exit 1

	fi


}



#Prototype via so many options and encryption standards
encrypt() {

echo -e " "
exit 0
#file luks keyfiles
#Create a keyfile to recieve random data from dd touch /media/user/usbmount/keyfile
#Copy keyfile for luks sudo dd bs=512 count=4 if=/dev/random of=/media/user/testmount/mykey iflag=fullblock

#Next Create openssl (Can be improved upon...) key via rsa 4096 bit on keyfile
#openssl genrsa -out /media/whftf/testmount/mykey 4096 

#mod perms on keyfile to nottt allow other people to edit


#chmod -v 0400 /media/user/testmount/mykeyfile
#chown -v root:root /media/user/testmount/mykeyfile
#Overwrite mounted device after clearing system


}

#Prototype for verbose mode for logging stderr, hw (lspci, lsusb, dmseg) logging info etc
cfunc() {

	testme=$(echo $?)
	# -eq ---- check if integer is equal
	if [[ "$verb" -eq 1 ]]; then
		echo "Verbose mode on"
		exit 0

	else
		exit 1

	fi

}

#Get options
## ;; --- is comma / seperator
# >&2 -- sending output to stderr instead of stdout
#Clause for getops is while getopts var with any
#param taking an input getting a : after.
while getopts "fbhw:c:" opt; do

	case $opt in 
	f)
		findusb
		;;

	b)
		echo "Test b"
		;;

	w)
		wipe
		;;


	c)
		verb="$OPTARG"
		cfunc
		;;


	h)
		helpfunc
		;;

	#escape edge case
	\?)
		echo "Not valid argument..... -$OPTARG " >&2
		sleep 0.8
		echo -e "\n\n Please use the $dirrn/EncryptUsb.sh -h for command assistance \n"
		echo -e "\n" && helpfunc
		exit 1
		;; 

	esac

done




#Double  quote to avoid word splitting
shift "$((OPTIND - 1))"






