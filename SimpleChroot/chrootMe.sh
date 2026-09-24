#!/usr/bin/env bash
rooot=$(echo -e "$UID")
pwdd=$(pwd)
chr=$(chroot recover/)
if [[ "$root" -ne 0 ]]; then 
	echo -e "Please run as root" && exit 1; 
else 
	echo -e "Creating directory recover/ in $pwdd "
	mkdir -p recover
	echo -e "Now.. find correct partitions to mount..." && sleep 1.5
	fdisk -l | grep -iE "/dev/nvme*|/dev/sd*" || lsblk -l
	read -p "Enter EFI partition: (e.g. /dev/nvmexySp1): " efi
	read -p "Enter Broken Partition you are aiming to mount & recover here: " broken
	if mount | grep "^$broken" && mount | grep "^efi"; then
		echo -e "Partitions found.... "
		echo -e "Mounting other required filesystems... "
		mount -t proc proc recover/proc
		mount -t sysfs sys recover/sys
		mount -o bind /dev recover/dev
		mount -t devpts pts recover/dev/pts
		if "$chr"; then
			echo -e "Chroot Successful!"
			ls -lah && pwd
			exit 0
		fi
	else
		echo -e "Drives not found... please reselect and try again"
	fi
fi

