#!/usr/bin/env python3

from termcolor import colored
import argparse
import subprocess
import re

def create_arguments():
    parser = argparse.ArgumentParser(description="Change your MAC address")
    parser.add_argument('-i','--interface',dest="interface",required=True,help='Insert the interface (ej. eth0, enp3s0)')
    parser.add_argument('-m','--mac',dest="mac",required=True,help="Insert the new mac address (ej. XX:XX:XX:XX:XX:XX)")

    return parser.parse_args()

def is_valid_input(interface, mac):
    
    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interface)
    is_valid_mac_address = re.match(r'^([a-fA-F0-9]{2}[:]){5}[a-fA-F0-9]{2}$', mac)
    
    return is_valid_interface and is_valid_mac_address

def change_mac_address(interface, mac):

    if is_valid_input(interface, mac):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac])
        subprocess.run(["ifconfig", interface, "up"])

        print(colored(f"\n[+] La MAC ha sido cambiada exitosamente \n","green"))
        
    else:
        print(colored("\n[-] Los datos introducidos son incorrectos","red"))

def main():
    args = create_arguments()
    change_mac_address(args.interface,args.mac)

if __name__ == '__main__':
    main()
