IP4_PARAMS = { 
    'net.ipv4.conf.default.accept_redirects' : "0", 
    'net.inet.ip.linklocal.in.allowbadttl' : "0", 
    'net.ipv4.ip_forward' : "0", 
    'net.ipv4.tcp_syncookies' : "1",
    'net.ipv4.conf.all.accept_redirects' : "0",
    #This enables TCP SYN Cookie Protection for IPv4 and IPv6
    #Small CPU tradeoff to disallow for dropping all unallocated connections via tcp when no further tcp connections can be accepted the normal way
    #We then instead avoid the entire non tcp protocol compliant stuff and employs a fallback tcp algo for overloaded connections
    #Works against our favor if high amopunts of tcp connections
    'net.ipv4.tcp_max_syn_backlog' : "4096",
    'net.ipv4.conf.default.accept_source_route' : "0",
    'net.ipv4.conf.all.accept_source_route' : "0", 
    'net.ipv4.conf.all.secure_redirects' : "0", 
    'net.ipv4.conf.all.log_martians' : "0", 
    'net.ipv4.conf.default.log_martians' : "0", 
    'net.ipv4.icmp_echo_ignore_broadcasts' : "1", 
    'net.ipv4.icmp_ignore_bogus_error_responses' : "0",
    'net.ipv4.conf.default.send_redirects' : "0",
    'net.ipv4.conf.all.send_redirects' : "0" 
}



IP6_PARAMS = {
    'net.ipv6.conf.default.accept_redirects' : "0",
    'net.ipv6.conf.all.accept_redirects' : "0"

}


KERNAL_PARAMS = {

	 'kernel.yama.ptrace_scope', 
        'fs.protected_fifos', 
        'fs.protected_hardlinks',
         'fs.protected_regular', 
         'fs.protected_symlinks', 
         'fs.suid_dumpable', 
         'kernel.core_uses_pid', 
         'kernel.apparmor_restrict_unprivileged_unconfined

    
}
