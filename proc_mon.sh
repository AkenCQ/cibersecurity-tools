#!/bin/bash

trap 'echo -e "\nMonitorización detenida."; exit 0' SIGINT SIGTERM

get_procs() {
    ps -eo pid,user,args --no-headers | grep -vE "ps -eo|grep -vE|sleep|kworker|processComp"
}

old_procs="$(get_procs)"

echo "Iniciando monitorización de procesos... (Ctrl+C para salir)"

while true; do
    sleep 1
    new_procs="$(get_procs)"
    
    comm -13 <(echo "$old_procs" | sort) <(echo "$new_procs" | sort) | while read -r line; do
        echo -e "[+] \033[0;32mNUEVO\033[0m   $(date +'%T') | $line"
    done
    
    comm -23 <(echo "$old_procs" | sort) <(echo "$new_procs" | sort) | while read -r line; do
        echo -e "[-] \033[0;31mMUERTO\033[0m   $(date +'%T') | $line"
    done
    
    old_procs="$new_procs"
done
