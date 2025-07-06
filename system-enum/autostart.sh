#!/bin/bash

#Script for starting kali with bashrc


sudo ip link set dev wlan0 down
sudo ip link set dev eth0 down
sudo macchanger -b -r eth0
sudo ip link set dev eth0 up
sudo ip6tables -P INPUT DROP
sudo ip6tables -P FORWARD DROP
sudo ip6tables -P OUTPUT DROP 
sudo systemctl stop wpa_supplicant.service
sudo systemctl stop NetworkManager
sudo systemctl restart auditd
if command -v libvirtd; then 
	sudo systemctl restart libvirtd
fi
#General inspection commands
uname -a
sleep 1
df -h
df -ah
sleep 1
fdisk -l
sleep 1
dpkg --get-selections
sleep 2
w
sleep 1
who -a
sleep 1
id
sleep 1
last -a
sleep 1
ps -ef | grep user

#File to autoclean with apt

sudo apt-get autoremove
sudo apt-get autoclean
doas apt-get check
doas apt-get autopurge
