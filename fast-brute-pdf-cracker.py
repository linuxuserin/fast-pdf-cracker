#################################################################################
#                                                                           	#
#   This script is written by Injamul Mohammad Mollah                           #
#   copyright 2020 Injamul Mohammad Mollah <mrinjamul@gmail.com>                #
#   under licensed MIT                                                          #
#   Disclaimer: The program is written for Education purpose only.              #
#   I’ll not be responsible for any direct or indirect damage caused            #
#    due to the usage of the program application.                               #
#                                                                           	#
#################################################################################

#!/usr/bin/env python3

import pikepdf
import time,os,sys
import itertools

Banner = """
   __               _        ___                     _               
  / _|  __ _   ___ | |_     / __|  _ _   __ _   __  | |__  ___   _ _ 
 |  _| / _` | (_-< |  _|   | (__  | '_| / _` | / _| | / / / -_) | '_|
 |_|   \__,_| /__/  \__|    \___| |_|   \__,_| \__| |_\_\ \___| |_|  
                                                                     
"""

def brute():
    arg1 = str(sys.argv[1])
    alphabet = ""
    length = 0
    try:
        alphabet = input("Enter the list(case sensitive):")
    except:
        pass
    try:
        length = int(input("Enter the length:"))
    except:
        pass

    if alphabet == "":
        alphabet = " 0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz;!@#$%^&*()_-+={}[]|\”:?/"
        print("You have not entered any list...")
        print("[*] Trying default list...(not recommanded)")
        time.sleep(2)

    if length == 0:
        length = len(alphabet)

    start = time.time()
    flag=0
    tryn = 0
    for a in range(1,length+1):
        for b in itertools.product(alphabet,repeat=a):
            k="".join(b)
            tryn+=1
            print("[*] Trying " + str(tryn) + " :" + str(k))
            password=k
            try:
                with pikepdf.open(arg1, password=k) as pdf:
                    print("[+] Password found: ", k)
                    flag = 0
                    print("Tried combination count:",tryn)
                    print("It took",round(time.time()-start,3),"seconds")
                    break
            except pikepdf._qpdf.PasswordError as e:
                flag = 1
                continue

    if flag == 1:
        print("It took",round(time.time()-start,3),"seconds")
        print("[-] Password not found. ")


def dict():
    arg1 = str(sys.argv[1])
    arg2 = str(sys.argv[2])
    start = time.time()
    flag=0
    # passwords = [ line.strip() for line in open(arg2) ]
    cp = ""
    print("Decrypting PDF......")
    tryn = 0
    # iterate over passwords
    with open(arg2) as passwords:
        for password in passwords:
            try:
                password = password.strip()
                tryn += 1
                print("[*] Trying " + str(tryn) + " :" + str(password))
                with pikepdf.open(arg1, password=password) as pdf:
                    # Password decrypted successfully, break out of the loop
                    cp = password
                    flag = 0
                    break
            except pikepdf._qpdf.PasswordError as e:
                # wrong password, just continue in the loop
                flag = 1
                continue
    if flag == 0:
    	print("[+] Password found:", password)
    	print("Tried combination count:",tryn)
    	print("It took",round(time.time()-start,3),"seconds")
    	print("Exiting...")
    else:
        print("It took",round(time.time()-start,3),"seconds")
        print("[-] Password not found. ")
    


if __name__ == "__main__":
    print(Banner)
    time.sleep(1)
    # noob = input("Press enter to continue...")
    arg1 = None
    arg2 = None
    try:
        arg1 = str(sys.argv[1])
        arg2 = str(sys.argv[2])
    except:
        pass
    if arg1 == None:
        print("Usages: ./"+ str(sys.argv[0]) + " [filename]")
        print("or")
        print("Usages: ./"+ str(sys.argv[0]) + " [filename] [wordlist]")
        exit(0)
    if arg2 == None:
        brute()
    else:
        dict()
