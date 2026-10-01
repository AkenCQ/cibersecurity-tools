#!/bin/bash

trap 'echo -e "\nMonitorización detenida."; exit 0' SIGINT SIGTERM
old_process="$(ps -eo user,command)"

echo "Iniciando monitorización de procesos... (Ctrl+C para salir)"
while true; do
    new_process="$(ps -eo user,command)"
    diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | -vE "procmon|kworker"
done
