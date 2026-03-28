#!/usr/bin/env bash

#Script by; Alexander Carter
##What is this? This util script automates configuring a killswitch for TOR, ensuring network traffic out of eth0 or wlan0 cannot reach outside our loopback address without going thru Tor Circuts, with either TCP initiating connecitons, or any udp DNS connections. Overall, this script aims to reduce the liklehood of an outbound leak from browsing while using tor, as traffic is forced thru the specified tor routing within /etc/tor/torrc. 
## Other then setting up an entire ip route table statically, and using MANGLE table to mark and track packets, this is the next best layer of denying leaking connections (WebRTC, DNS, IPv6, NTP, etc). 

###Global Vars
TRANS_PORT=9043
DNS_PORT=9053
LO_IFACE=lo
TOR_UID=$(id -u toranon)

echo -e "Starting Script"
uid=$(id -u "$USER")
if [ "$uid" != 0 ]; then
	echo -e "Please run as root." && exit 1
fi


clearRules() {
	##Logic error here when we ask user to del rules, then we need to do it again w/ our logic no matter if they choose to clear cuz we have to call second functuion that calls the question, again...
        read -p "Clear iptables rules now? (y\n\l): " -en 1 addMore
        if [[ "$addMore" =~ y|Y ]]; then
		##Temp no PATH ensure
                iptables -F && iptables -X
                iptables -t nat -F
                iptables -t nat -X
		iptables -P INPUT ACCEPT
		iptables -P OUTPUT ACCEPT
		iptables -P FORWARD ACCEPT
		iptables -t nat -P OUTPUT ACCEPT
	elif [[ "$addMore" =~ l|L ]]; then
		echo -e "Listing rules.." && sleep 0.45
		clear
		iptables -L -v -n && iptables -t nat -L
		clearRules
        else
                echo -e "Skipping... "
		

        fi 

}

create_Our_Tor_Rules() {
	
	clearRules
	sleep 2
	echo -e "\n\n"
	echo -e "[*] Adding Rules Now"
	
	ip ad | grep -iw 'UP'
	echo -e "\n\n"
	read -p "Input Network Adapter Here: " nett
	##BASIC
	iptables -A INPUT -i lo -j ACCEPT 
	iptables -A OUTPUT -o lo -j ACCEPT
	##Allow traffic outbound from root, user uid, and tor uid
	##NOTE: Can allow traffic from --gid-owner for wheel (Not setup here)
	#iptables -A OUTPUT -m owner --uid-owner 0 -j ACCEPT
	#iptables -A OUTPUT -m owner --uid-owner 1000 -j ACCEPT
  ##Verbose NAT Logging, will be noisy, will update. Should show PoC redirects however
  iptables -t nat -A OUTPUT -j LOG --log-level=7 --log-prefix="REACHED NAT OUTBOUND CONNECTION!"
	iptables -t nat -A OUTPUT -m owner --uid-owner 1000 -j RETURN
	iptables -A OUTPUT -m owner --uid-owner 1000 -j RETURN
	##Continue down rule set if specific natted output is from uid toranon
  #iptables -t nat -A OUTPUT -p tcp -m owner --uid-owner  $TOR_UID -j RETURN
	iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT
	 #Ignore SSL/TLS as Tor is L3/4
  iptables -t nat -A OUTPUT -p tcp --dport 443 -j ACCEPT
	##Redirect all output of DNS traffic from destination port 53 to outbound ports 9053
	iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports $DNS_PORT
	#iptables -t nat -A OUTPUT -p tcp --dport 53 -j REDIRECT --to-ports $DNS_PORT
	##Redirect ALL tcp requests outbound (syn to mark newly initiated requests) to TRANSPORT (Transpartent Proxy Port)
	iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT
	##Track state, non user specific 
  iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
	iptables -A OUTPUT -j LOG --log-level=7 --log-prefix="REACHED OUTBOUND CONNECTION!"

	
	#OPTIONAL
	#declare -A questions=(
    	#	["Drop ICMP? (y/n): "]="-A OUTPUT -p icmp -j DROP"
	#	["Drop LAN Connections? (y/n): "]="-A INPUT "
	#	["Drop ICMP?"]="drop_icmp"
	#)

	#read -p "Harden LAN Options? (y/n): " -en 1 harden
	#if [[ "$harden" =~ y|Y ]]; then
	iptables -A OUTPUT -i $nett -p icmp -j DROP
	iptables -A INPUT -i $nett -p icmp -j DROP 
	iptables -P OUTPUT DROP 
	iptables -P INPUT DROP
	ip6tables -P INPUT DROP 
	ip6tables -P OUTPUT DROP
	ip6tables -P FORWARD DROP

	clear && echo -e "New Rules: "
	iptables -L -v -n && iptables -t nat -L -v -n



}



Help() {

	echo -e "[*] Options to run with script... "
	echo -e "----------------------------------------------------------------------------------------------------------"
	echo -e "[*] -h -- Help Menu Like you are seeing now! "
	echo -e "[*] -t -- Automate iptables flushing // rule appendage via nat rules! Prevents Leaks outside tor OUTBOUND" 
	echo -e "[*] -h -- Help Menu Like you are seeing now! " 
	echo -e "[*] -h -- Help Menu Like you are seeing now! " 
	echo -e "[*] -h -- Help Menu Like you are seeing now! "  
	echo -e "----------------------------------------------------------------------------------------------------------"

}

##TORRC EXAMPLE CONFIG STRUCUTRE:
#Control Socket:
#ControlSocket /run/tor/control
#ControlSocketsGroupWritable 0
#Cookie Auth if selected (Default)
#CookieAuthentication 1
#CookieAuthFile /run/tor/control.authcookie
#CookieAuthFileGroupReadable 1
#SOCKSPort 127.0.0.1:9050 #Regular SOCKS5 Proxy
#DNSPort 127.0.0.1:9053 #DNS Listening proxy (masquerade pt 53 => 9053)
#TransPort 127.0.0.1:9043 #Transport is transparent proxy for TCP (L3/4)
#SOCKSPolicy accept 127.0.0.1 
##SOCKSPolicy accept6 FC00::/7
#SOCKSPolicy reject *
#AutomapHostsOnResolve 1 #Resolve dns thru tor
#NewCircuitPeriod 10 # Quick reset of circuts
#MaxCircuitDirtiness 60
#Log debug stderr -- if you want



##NOTE: For SE_Linux, you aren't able to assign empherial or unregistered ports all willy nilly (RHEL has specifc se-commands for this)

##sudo semanage boolean -l -C => List all locally assigned selinux policies
#sudo semanage boolean -m tor_bind_all_unreserved_ports --on => Enable or Disable a specific policy
#sudo semanage port -a -t tor_port_t -p tcp 9053 => Add a specific port to se linux profile, this is transport example


##Take in options #:)
while getopts "ht" opt; do
    case $opt in
        h) Help ;;
        t) create_Our_Tor_Rules ;;
        #c) Verbose=true ;;
        ?) echo "Unknown option... use -h for help options :)"; exit 1 ;;
	*) create_Our_Tor_Rules ;;
    esac
done
shift $((OPTIND - 1))
