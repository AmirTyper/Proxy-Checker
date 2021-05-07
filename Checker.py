# coding: utf-8
from platform import python_version
if int(python_version()[0]) < 3:
    print("[!] Please use Python 3")
    exit()
'''
      Coded: By Amir Typer 
      --------------------|
      Istagram: amir_typer
      Telegram: Mr_Amir_Typer
      Twitter: Amir_Typer
      GitHub: https://github.com/Amirtyper
      |--------------------
      Version : 1.0
      Date: 5/8/2021
      Date (Persian Calendar): 1400/2/18
'''
import requests
import random
import time
#import threading
import os
import sys
os.system("clear")
welcome = """
|||||            ~ Proxy Checker ~            |||||
 ||||        Coded By : @Mr_Amir_Typer        ||||
  |||        Our Channel : @Sezar_Hack        |||
   ||        ©Powered By : NowaTech.ir        ||
    |                    V1                   |
"""
print(welcome)
# Startup 1
try:
    inp = input("|- Open proxy file -->: ")
except:
    b = input("[!] Error! Proxy file is not exist or it's empty.\n|- Would you like to run script again? --> y/N : ")
    if "Y" == b or "y" == b:
        print ("Restarting...")
        time.sleep(2)
        os.system("python Checker.py")
        os.system("clear")
        sys.exit()
    if "N" == b or "n" == b:
        print("|- OK, Bye!")
        sys.exit()
    else:
        time.sleep(1)
        print("[!] Error! Only write Y or N.\n|- Restarting the script in 3 seconds..")
        time.sleep(3)
        os.system("python Checker.py")
        os.system("clear")
        sys.exit()
# Startup 2
try:
    addr = str(input("|-- Do you have any exclusive URL in your mind? (Press ENTER for Default) -->: "))
    addr2 = addr
    if addr == "":
        addr = "https://google.com"
    elif "http://" or "https://" not in addr:
        addr= "http://"+addr2
    #numberofthreads = int(input("|-- Threads -->: "))
    timeout = int(input("|--- Timeout -->: "))
    inp2 = input("|---- Would you like to save good proxies in a file? --> y/N : ")
except:
    time.sleep(1)
    print("[!] Error! Only write the Number Or Type URL With HTTP:// Or HTTPS:// .\n|- Restarting the script in 3 seconds..")
    time.sleep(3)
    os.system("python Checker.py")
    os.system("clear")
    sys.exit()
if "N" == inp2 or "n" == inp2:
    print("|- OK")
def Check():
    # Read And Open Proxy File
    filepath = inp
    with open(filepath) as fp:
        lines = fp.read().splitlines()
    with open(filepath, "r") as fp:
        # Count Proxies
        line_count = 0
        for i in lines:
            if i:
                line_count += 1
        time.sleep(1)
        print("|----- Count of loaded proxies --> :",line_count)
        #----------------
        time.sleep(1.5)
        print(">------ Start Checking in Two Second ------<\n")
        time.sleep(2)
        for line in lines:
            proxy = ("http://"+line)
            try:
                # Send Request 
                headers = {
                "accept": "*/*",
                "user-agent": "Mozilla/5.0",
                }
                response = requests.get(addr ,headers=headers,timeout=timeout,proxies={"http://":tuple(random.sample(proxy, len(line)))})
                #----------------
                # Check Response and Write good proxies in a file
                if "Y" == inp2 or "y" == inp2:
                    f = open("Good Proxies.txt", "a")
                    f.write(proxy.replace("http://","")+"\n")
                    f.close()
                    print("[-] Working ["+str(response.status_code)+"] | Proxy --> "+proxy.replace("http://",""))
                else:
                    time.sleep(1)
                    print("[!] Error! Only write Y or N.\n|- Restarting the script in 3 seconds..")
                    time.sleep(3)
                    os.system("python Checker.py")
                    os.system("clear")
                    sys.exit()
            except requests.exceptions.Timeout: 
                print ("[~] Request timed out. | Proxy failed --> "+proxy.replace("http://",""))
            except:
                print("[!] Error! Check your internet connection and run script again.")
                sys.exit()
                #----------------
    # All Done
    print("\n[✓] Done! All Proxies Are Checked - Good Proxies Saved In A File [✓]\n")
    sys.exit()
Check()
# threads = [] 
# for i in range(numberofthreads):
#     t = threading.Thread(target=Check)
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
