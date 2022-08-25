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
 {Green}     ||             {Purple}==>{Yellow}[1] Insta information gathering{Green}                    ||
 {Green}     ||             {Purple}==>️{Yellow}[️2] Insta brute force attack{Green}                       ||
 {Green}     ||             {Purple}==>{Yellow}[3] Insta auto reporter{Green}                            ||
 {Green}     ||             {Purple}==>{Yellow}[4] Insta phishing page(coming soon){Green}               ||
 {Green}     ||             {Purple}==>{Yellow}[5] Update script{Green}                                  ||
 {Green}     ||             {Purple}==>{Yellow}[6] Remove script{Green}                                  ||
 {Green}     ||             {Purple}==>{Yellow}[️7] About{Green}                                          ||
 {Green}     ||             {Purple}==>{Yellow}[x] exit{Green}                                           ||
 {Green}     ||                                                                   ||
 {Green}     ||---------------------------{Cyan} [select option] {Green}-----------------------||
 {Green}     |---------------------------------------------------------------------|''')
print("\n")
ch = int(input("\033[1;36mSelect Option >>> "))
if ch == 1:
    os.system("cd $HOME")
    os.system("cd insta-hack")
    os.system("cd Ig_information_gathering")
    os.system("bash start.sh")
if ch == 2:
    os.system("cd $HOME")
    os.system("git clone https://github.com/noob-hackers/ighack")
    os.system("cd $HOME/insta-hack/ig_brute_force")
    os.system("bash setup")
    os.system("bash ighack.sh")
elif [ $ch -eq 3 ];then
git clone https://github.com/Crevils/InstaReport
cd InstaReport
pip install -r requirements.txt
python ReportBot.py
exit
elif [ $ch -eq 4 ];then
os.system("cd $HOME")
echo "Coming Soon!\n"
exit
elif [ $ch -eq 5 ];then
echo -e "\e[1;34m Downloading Latest Files..."
os.system("cd $HOME")
rm -rf insta-hack
git clone https://github.com/HackerSM9/insta-hack
cd insta-hack
bash insta-hack.sh
exit
elif [ $ch -eq 6 ];then
os.system("cd $HOME")
rm -rf insta-hack
exit
elif [ $ch -eq 7 ];then
echo -e
os.system("cd $HOME")
exit
elif [ $ch -eq x ];then
echo "Exited Successfully !!!\n"
os.system("cd $HOME")
exit
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
fi
