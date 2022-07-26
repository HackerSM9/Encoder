#bin/python
#Author: HackerSM9
import os
import time
import sys
import colorama

CY= '\033[1;34m'
B= '\033[0;90m'
S= '\033[0;91m'
C= '\033[1;37m'
ki= '\033[0;60m'
about= "\033[0;89mThis tool will help you in installing required packages for my tool"
os.system("cls || clear") 
print(CY+ "This script will help you in installing required packages for Encoder script") 
time.sleep(3)
os.system("pkg install git python2 python3 -y") 
os.system("pip install lolcat") 
os.system("apt install figlet") 
os.system("pkg install wget && pkg install curl && pkg install clang && pkg install zip unzip -y") 
os.system("cd $HOME") 
os.system("cd Encoder") 
os.system("cls || clear")
print(S+ "All packages have been successfully installed ") 
print("") 
print(C+ "Thanks for using this tool made by HackerSM9")
print("")
time.sleep(2)
print("For Encoding Shell code use encrypt.py\nFor Encoding Python code use encode.sh\n\n") 
