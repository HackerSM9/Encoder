import os,sys
import time

Black="\033[1;30m"     
Red="\033[1;31m"        
Green="\033[1;32m"     
Yellow="\033[1;33m"    
Blue="\033[1;34m"       
Purple="\033[1;35m"    
Cyan="\033[1;36m"      
White="\033[1;37m"
 
os.system("clear")
print(f"{Purple} Created By {Blue}")
os.system("toilet -f ivrit HackerSM9 | lolcat")
time.sleep(2)
os.system("toilet -f ivrit Insta-Hack | lolcat")
print("")
print(f'''{Red}                                 ⫸ Coded by{Yellow} HackerSM9{Red} ⫷\033[0m
{Red}                         ⫸{Purple} Hacker | Developer | Programmer {Red}⫷\033[0m

 {Green}     |---------------------------------------------------------------------|
 {Green}     ||----------------------------{Cyan} [features] {Green}---------------------------||
 {Green}     ||                                                                   ||
 {Green}     ||             {Purple}==>{Yellow}[1] Insta Information Gathering{Green}                    ||
 {Green}     ||             {Purple}==>️{Yellow}[️2] Insta brute force attack{Green}                       ||
 {Green}     ||             {Purple}==>{Yellow}[3] Insta auto reporter{Green}                            ||
 {Green}     ||             {Purple}==>{Yellow}[4] Insta Information Gathering 2{Green}                  ||
 {Green}     ||             {Purple}==>{Yellow}[5] Update script{Green}                                  ||
 {Green}     ||             {Purple}==>{Yellow}[6] Remove script{Green}                                  ||
 {Green}     ||             {Purple}==>{Yellow}[️7] About{Green}                                          ||
 {Green}     ||             {Purple}==>{Yellow}[0] exit{Green}                                           ||
 {Green}     ||                                                                   ||
 {Green}     ||---------------------------{Cyan} [select option] {Green}-----------------------||
 {Green}     |---------------------------------------------------------------------|''')
print("\n")
ch = int(input("\033[1;36mSelect Option >>> "))
if ch == 1:
    os.system("cd && cd insta-hack && cd Ig_information_gathering && bash start.sh")
if ch == 2:
    os.system("cd && git clone https://github.com/noob-hackers/ighack && cd $HOME/insta-hack/ig_brute_force && bash setup && bash ighack.sh")
if ch == 3:
    os.system("git clone https://github.com/Crevils/InstaReport && cd InstaReport && pip install -r requirements.txt && python ReportBot.py")
if ch == 4:
    os.system("cd && cd insta-hack && python3 .page.py")
if ch == 5:
    print("\033[1;34m Downloading Latest Files...")
    os.system("cd $HOME && rm -rf insta-hack && git clone https://github.com/HackerSM9/insta-hack && cd insta-hack && bash insta-hack.sh")
if ch == 6:
    os.system("cd $HOME && rm -rf insta-hack")
if ch == 7:
    os.system("xdg-open https://github.com/HackerSM9/")
if ch == 0:
    print("\nExited Successfully !!!\n")
elif (ch >= 8):
    print("\033[4;32m Invalid Input !!! \033[0m")
else:
    print(Cyan+"\nDone! \n")
