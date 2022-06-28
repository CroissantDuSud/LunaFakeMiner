import time
from tkinter import mainloop
import colorama
from colorama import Fore
from colorama import Style
import random
import string 
import os
# ETH DOGE BTC USDT Fake Miner # 

os.system("cls")
banner = Fore.MAGENTA + """

 ██╗     ██╗   ██╗███╗   ██╗ █████╗     ███╗   ███╗██╗███╗   ██╗███████╗██████╗ ™
 ██║     ██║   ██║████╗  ██║██╔══██╗    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗  
 ██║     ██║   ██║██╔██╗ ██║███████║    ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝   
 ██║     ██║   ██║██║╚██╗██║██╔══██║    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗   
 ███████╗╚██████╔╝██║ ╚████║██║  ██║    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║  
 ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                                                                                                               
"""
print(banner)

crypto = str(input(Fore.WHITE + 'Choose between' + Fore.MAGENTA + ' ETH, BTC, DOGE, USDT ' + Fore.WHITE + ': '))

if crypto == 'ETH' or crypto == 'BTC' or crypto == 'info' or crypto == 'DOGE' or crypto == 'USDT':
    print(Fore.WHITE + "Please wait...")
    time.sleep(2)

    if crypto == 'ETH':
        print("")
        print(Fore.MAGENTA + "")
        print(" ███████╗████████╗██╗  ██╗")
        print(" ██╔════╝╚══██╔══╝██║  ██║")
        print(" █████╗     ██║   ███████║")
        print(" ██╔══╝     ██║   ██╔══██║")
        print(" ███████╗   ██║   ██║  ██║")
        print(" ╚══════╝   ╚═╝   ╚═╝  ╚═╝")
        adress = str(input(Fore.WHITE + "Please enter your Ethereum adress: "))
        print("Check if Wallet exist...")
        time.sleep(3)
        print("Check succesfully!")
        time.sleep(1)
        print("Lunching...")
        print("")
        time.sleep(3.7)

    elif crypto == 'BTC':
        print("")
        print(Fore.MAGENTA + "")
        print(" ██████╗ ████████╗ ██████╗")
        print(" ██╔══██╗╚══██╔══╝██╔════╝")
        print(" ██████╔╝   ██║   ██║     ")
        print(" ██╔══██╗   ██║   ██║     ")
        print(" ██████╔╝   ██║   ╚██████╗")
        print(" ╚═════╝    ╚═╝    ╚═════╝")
        adress = str(input(Fore.WHITE + "Please enter your Bitcoin adress: "))
        print("Check if Wallet exist...")
        time.sleep(3)
        print("Check succesfully!")
        time.sleep(1)
        print("Lunching...")
        print("")
        time.sleep(3.7)

    elif crypto == 'DOGE':
        print("")
        print(Fore.MAGENTA + "")
        print(" ██████╗  ██████╗  ██████╗ ███████╗")
        print(" ██╔══██╗██╔═══██╗██╔════╝ ██╔════╝")
        print(" ██║  ██║██║   ██║██║  ███╗█████╗  ")
        print(" ██║  ██║██║   ██║██║   ██║██╔══╝  ")
        print(" ██████╔╝╚██████╔╝╚██████╔╝███████╗")
        print(" ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝")
        adress = str(input(Fore.WHITE + "Please enter your Dogecoin adress: "))
        print("Check if Wallet exist...")
        time.sleep(3)
        print("Check succesfully!")
        time.sleep(1)
        print("Lunching...")
        print("")
        time.sleep(3.7)

    elif crypto == 'USDT':
        print("")
        print(Fore.MAGENTA + "")
        print(" ██╗   ██╗███████╗██████╗ ████████╗")
        print(" ██║   ██║██╔════╝██╔══██╗╚══██╔══╝")
        print(" ██║   ██║███████╗██║  ██║   ██║   ")
        print(" ██║   ██║╚════██║██║  ██║   ██║   ")
        print(" ╚██████╔╝███████║██████╔╝   ██║   ")
        print("  ╚═════╝ ╚══════╝╚═════╝    ╚═╝   ")
        adress = str(input(Fore.WHITE + "Please enter your Tether adress: "))
        print("Check if Wallet exist...")
        time.sleep(3)
        print("Check succesfully!")
        time.sleep(1)
        print("Lunching...")
        print("")
        time.sleep(3.7)



    elif crypto == 'info':
        print("")
        print(Fore.MAGENTA + "")
        print(" ██╗███╗   ██╗███████╗ ██████╗ ")
        print(" ██║████╗  ██║██╔════╝██╔═══██╗")
        print(" ██║██╔██╗ ██║█████╗  ██║   ██║")
        print(" ██║██║╚██╗██║██╔══╝  ██║   ██║")
        print(" ██║██║ ╚████║██║     ╚██████╔╝")
        print(" ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ")
        print("")
        print("Luna Fake Miner")
        print("")
        print("DEV by CroissantDuSud")
        print("Version: Beta | 28/06/2022 ")
        time.sleep(30)

    class bcolors:
        won = '\033[92m'
        fail = '\033[91m'

    def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    tries = 0

    if crypto == 'ETH':
        colorama.init()
        while(True):
            if(tries > random.randint(52456, 53593362)):
                print(Fore.GREEN + "]> 0x" + id_gen() + " |  Valid  | " + "0.173 ETH")
                print("Transfer 0.123 ETH to", adress)
                time.sleep(7.2)
                tries = 0
                print("Done! Miner Is running again!")
                print("")
                time.sleep(3.2)
            else:
                print(Fore.MAGENTA + "]> " + Fore.WHITE + "0x" + id_gen() + Fore.MAGENTA + " | " + Fore.RED + "Invalid" + Fore.MAGENTA + " | " + Fore.RED + "0.000 ETH")
                tries += 1

    if crypto == 'BTC':
        colorama.init()
        while(True):
            if(tries > random.randint(36357, 34526497)):
                print(Fore.GREEN + "]> bc1" + id_gen() + " |  Valid  | " + "0.145 BTC")
                print("Transfer 0.145 BTC to", adress)
                time.sleep(6.2)
                tries = 0
                print("Done! Miner Is running again!")
                print("")
                time.sleep(3.2)
            else:
                print(Fore.MAGENTA + "]> " + Fore.WHITE + "bc1" + id_gen() + Fore.MAGENTA + " | " + Fore.RED + "Invalid" + Fore.MAGENTA + " | " + Fore.RED + "0.000 BTC")
                tries += 1

    if crypto == 'DOGE':
        colorama.init()
        while(True):
            if(tries > random.randint(33367, 34536556)):
                print(Fore.GREEN + "]> do2" + id_gen() + " |  Valid  | " + "0.538 DOGE")
                print("Transfer 0.538 BTC to", adress)
                time.sleep(6.2)
                tries = 0
                print("Done! Miner Is running again!")
                print("")
                time.sleep(3.2)
            else:
                print(Fore.MAGENTA + "]> " + Fore.WHITE + "do2" + id_gen() + Fore.MAGENTA + " | " + Fore.RED + "Invalid" + Fore.MAGENTA + " | " + Fore.RED + "0.000 DOGE")
                tries += 1

    if crypto == 'USDT':
        colorama.init()
        while(True):
            if(tries > random.randint(33367, 34536556)):
                print(Fore.GREEN + "]> us" + id_gen() + " |  Valid  | " + "0.138 USDT")
                print("Transfer 0.138 USDT to", adress)
                time.sleep(6.2)
                tries = 0
                print("Done! Miner Is running again!")
                print("")
                time.sleep(3.2)
            else:
                print(Fore.MAGENTA + "]> " + Fore.WHITE + "us" + id_gen() + Fore.MAGENTA + " | " + Fore.RED + "Invalid" + Fore.MAGENTA + " | " + Fore.RED + "0.000 USDT")
                tries += 1


else:
    print(Fore.RED + "Invalid currency. Please choose between 'ETH' 'DOGE' 'BTC' 'USDT' ")
    time.sleep(7)
