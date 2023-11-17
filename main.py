import random
import time
import pywhatkit
import datetime
import os
import colorama
from colorama import Fore, Style

def print_banner():
    colorama.init()
    print(Fore.YELLOW + r"""
 
  _   _    _    ____  ______   __  ____ ___ ____ _____ _   _ ____    _ __   __
 | | | |  / \  |  _ \|  _ \ \ / / | __ )_ _|  _ \_   _| | | |  _ \  / \\ \ / /
 | |_| | / _ \ | |_) | |_) \ V /  |  _ \| || |_) || | | |_| | | | |/ _ \\ V / 
 |  _  |/ ___ \|  __/|  __/ | |   | |_) | ||  _ < | | |  _  | |_| / ___ \| |  
 |_| |_/_/   \_\_|   |_|    |_|   |____/___|_| \_\|_| |_| |_|____/_/   \_\_|  
                                                                                   
                                                                
    """ + Style.RESET_ALL)

def print_hacker():
    print(Fore.BLUE + r"""
 
'##::::'##::::'###:::::'######::'##:::'##:'########:'########::
 ##:::: ##:::'## ##:::'##... ##: ##::'##:: ##.....:: ##.... ##:
 ##:::: ##::'##:. ##:: ##:::..:: ##:'##::: ##::::::: ##:::: ##:
 #########:'##:::. ##: ##::::::: #####:::: ######::: ########::
 ##.... ##: #########: ##::::::: ##. ##::: ##...:::: ##.. ##:::
 ##:::: ##: ##.... ##: ##::: ##: ##:. ##:: ##::::::: ##::. ##::
 ##:::: ##: ##:::: ##:. ######:: ##::. ##: ########: ##:::. ##:
..:::::..::..:::::..:::......:::..::::..::........::..:::::..::
 
    """ + Style.RESET_ALL)

print_banner()



user =  input("enter birthday boy | girl name :")  #  enter name 
timeh = (datetime.datetime.now().hour)
timem = (datetime.datetime.now().minute)
timem +=1
        # Send a wish to your birthday on WhatsApp
def loop():
     gif = ["😍😍😍😍😍😍😍😍😍😍😍😍😍","🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰","🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳 "]
     g = random.choice(gif)
     pywhatkit.sendwhatmsg("+91enter your number", "Happy birthday   {} 🎂🎂🎂🎂 {}".format(user,g) , timeh, timem)


###################  made by khilesh    ##################
##########################################################


print_hacker()
loop()