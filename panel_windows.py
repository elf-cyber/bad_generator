
import socket
import os ,tqdm
ClientSocket = socket.socket()
host = ''
port = 

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

    