# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="agnosterzak"

plugins=( 
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh


echo -e "\n\n"
BOLD='\e[1m'
RESET='\e[0m'
GREEN='\e[032m'
alias ls='lsd'
alias l='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'
alias code='flatpak run com.visualstudio.code'
alias updateme='sudo apt-get update -y && sudo apt-get upgrade --show-progress -y'

echo -e "$BOLD"
echo -e "Commands and Aliases.... "
echo -e "Extracting files: "
echo -e "TAR FILES: tar -xvf "
echo -e "TAR.GZ FILES: tar -xzvf file.tar.gz "
echo -e "REGULAR .GZ FILES: gunzip file.gz "
echo -e "XZ FILES: unxz or xz -k -d file.xz "
echo -e "STANDALONE XZ FILES: xz -d filename.xz "
echo -e ".ZIP FILES: unzip file.zip "
echo -e "WORKING WITH .DEB FILES: dpkg -i /path/to/file.deb "
echo -e "THEN RUN sudo apt install ./package_name.deb to install .deb file \n\n "
echo -e "general kernal info: uname --all "
echo -e "Overview on specific Port usage: ss -tulpn "
echo -e "Another Overview on port specifics: netstat -tunlp "
echo -e "code ---- flatpak run com.visualstudio.code  "
echo -e "snap find ---- to search for snap packages "
echo -e "Working with checksum/hash verification: \n "
echo -e "sha256sum --ignore-missing -c Fedora-Workstation-42-1.1-x86_64-CHECKSUM "
echo -e "DISABLING THE KVM KERNAL MODULES PREVENTING VBOX "
echo -e "#1 sudo modprobe -r kvm_intel "
echo -e "#2 sudo modprobe -r kvm "
echo -e "Remember /etc/hosts "
echo -e "df -Bg -h "
echo -e "file command for easy checking of existence "
echo -e "Launch VirtualBox vm with debug enabled: virtualbox --startvm 'debnet' --dbgvir"
echo -e "Command to run to dump vbox memory: .pgmphystofile <nameoffile> "
echo -e "Anifetch Command (Must Be Root!!): anifetch Downloads/ASCIIART/giphy.gif  -r 10 -W 80 -H 120 -c --symbols narrow --colors=256 -w 9 --symbols all --size 300x450  -ff -fr -pr 8 --chroma 2>/dev/null"
echo -e "BETTER FILE / FOLDER PERMISSION OUTPUT: sudo getfacl <folder/location>"
echo -e "Verbose output from apt update, showing sources and pgp keys of packages: sudo apt update -o Debug::Acquire::https=true " 
echo -e "Secure delete files, and re-write over mem and area on disk with rando data: shred -u -v -n=5 filename.txt -z -f"
echo -e "You can additionally secure wipe a partition with the above shred command (or shred -vfz /dev/sda "
echo -e "Potential APT NO PUBKEY FOUND per package fix: sudo apt-key adv --refresh-keys --keyserver keyserver.ubuntu.com"
echo -e "REGEX: Example Usage; find all log files associated to one package string and rm them: sudo find / -type f -regex '.*fire.*\.log'  -exec rm {} \; 2&>/dev/null "
echo -e "HackTrix Bible: docker run -d -p 3000:3000 djangobyjeffrey/hacktricks "
echo -e "Updating Grub (e.g. when updating app armor GRUB profile, or any general theme / update); "
echo -e "Update Grub After Changed Config: sudo update-grub "
echo -e "Update Grub On System w/ out update-grub: sudo grub-mkconfig -o /boot/grub/grub.cfg "
echo -e "Grabbing command logs from auth.logs: sudo cat /var/log/auth.log-20260208 | grep COMMAND | sort -u | uniq "
echo -e "Copy file to other dest. with checking bit checksum: rsync --checksum "
echo -e "Kill Something Via Specific Port: sudo kill -9 dollar parenth sudo lsof -t -i:PORT_NUMBER) "
echo -e "Extra DNS & LLMNR config per interfaces: /etc/systemd/resolved.conf  "
echo -e "$RESET"


if lsmod | grep -iw 'kvm' 2&>/dev/null; then

	echo "Disabling kvm kernel modules for vbox"
	sudo modprobe -r kvm_intel && sudo modprobe -r kvm && sudo systemctl daemon-reload

else
	echo " "

fi

check=$(sysctl -a | grep -iw "net.ipv6.conf.all.disable_ipv6"  | awk '{print $3}' 2&>/dev/null)
if [ "$check" != 1 ]; then
        echo -e " Disabling IPv6... "
	sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
	sudo ip6tables -P INPUT DROP
	sudo ip6tables -P OUTPUT DROP
	echo -e "Reading fstab and checking mounted disks...."
	if sudo lsblk -f -l |awk '{print $1}' |grep -P '^sd[a-z0-9]*$'; then
		echo -e "Automounting Ext Media based on fstab... "
		sudo mount -a 2&>/dev/null && sleep 2.5
		mountdir=$(mount -l | grep "/dev/sd" | awk '{print $3}')
		echo -e "[*] Mounted Directory Location: $mountdir "

	else


		echo "No mounted media found.. skipping"


	fi



else
        echo -e " "

fi

sleep 1
echo -e "\n\n\n\n"
clear
# Display Pokemon-colorscripts
# Project page: https://gitlab.com/phoneybadger/pokemon-colorscripts#on-other-distros-and-macos
#pokemon-colorscripts --no-title -s -r #without fastfetch
pokemon-colorscripts --no-title -s -r | fastfetch -c $HOME/.config/fastfetch/config-pokemon.jsonc --logo-type file-raw --logo-height 10 --logo-width 5 --logo -

# fastfetch. Will be disabled if above colorscript was chosen to install
#fastfetch -c $HOME/.config/fastfetch/config-compact.jsonc

# Set-up icons for files/directories in terminal using lsd


# Created by `pipx` on 2025-11-11 18:52:33
