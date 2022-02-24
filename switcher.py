#!/usr/bin/env python

from os import system as shell
import time
import argparse
from turtle import speed

shell('clear')

bar = [
    "[=         ]",
    "[ =        ]",
    "[  =       ]",
    "[   =      ]",
    "[    =     ]",
    "[     =    ]",
    "[      =   ]",
    "[       =  ]",
    "[        = ]",
    "[         =]",
    "[        = ]",
    "[       =  ]",
    "[      =   ]",
    "[     =    ]",
    "[    =     ]",
    "[   =      ]",
    "[  =       ]",
    "[ =        ]",
]

def barrita(tiempo):
    i = 0
    for i in range(0,tiempo):
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2) # time per frame
        i += 1

parser = argparse.ArgumentParser()

parser.add_argument('-c', required=True, help="country to search")
parser.add_argument('-speed', required=False, help="sleep between circuit connection [0 fast, 10 slow]")

args = parser.parse_args()

country = str(args.c).capitalize()
try:
    speed_custom = int(args.speed)
except:
    speed_custom = 0
    print('Using default speed [10x2]')

print('''  ____         
 |  _ \        
 | |_) | _   _ 
 |  _ < | | | |
 | |_) || |_| |
 |____/  \__, |
          __/ |
         |___/ 

███████╗████████╗██████╗        ██████╗████████╗██╗  ██╗
██╔════╝╚══██╔══╝██╔══██╗      ██╔════╝╚══██╔══╝╚██╗██╔╝
███████╗   ██║   ██║  ██║█████╗██║  ███╗  ██║    ╚███╔╝ 
╚════██║   ██║   ██║  ██║╚════╝██║   ██║  ██║    ██╔██╗ 
███████║   ██║   ██████╔╝      ╚██████╔╝  ██║   ██╔╝ ██╗
╚══════╝   ╚═╝   ╚═════╝        ╚═════╝   ╚═╝   ╚═╝  ╚═╝

''')

print(f'Finding a circuit ending in {country}')

print('Stoping Tor service...')
shell('service tor stop')
print('Starting connection...')
print('This may take a while dpending on avaliable tor circuites and internet connection')
print('Please be patient and dont quit the script')

shell('kalitorify -t > tor.temp')

def switch():
    shell('echo a > tor.temp; rm tor.temp;')
    shell('kalitorify -r > tor.temp')
    with open('tor.temp', 'r') as file:
        output = file.read().replace('\n', '')
    again = output.find(country)
    if again == -1:
        print('oops')
        for i in range(0, speed_custom):
            barrita(10)
            barrita(10)
        switch()
switch()
print(f'You´re now connected to {country}!')
#with open('tor.temp', 'r') as file:
#    output = file.read().replace('\n', '')
#again = output.find(country)
#print(again)  
#if again == -1:
#    print('oops')
#    barrita(10)
#    barrita(10)
    

#
#for i in range(0,1):
#    print(bar[i % len(bar)], end="\r")
#    time.sleep(.2) # time per frame
#    i += 1
