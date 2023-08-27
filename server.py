import socket
import threading

port=5050
servern=socket.gethostbyname(socket.gethostname()) 
print(socket.gethostname())
Addr=(servern,port)
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',port))

def start():
    server.listen()
    print(f"[listning] server is listning on server {servern}")
    while True:
        conn,addr =server.accept() 
        thread=threading.Thread(target=handle_client,args=(conn,addr)) 
        thread.start()
        print(f"[total active connections] {threading.activeCount()-1} ")




def handle_client(self,arg):
    print(f"[new connection]   {Addr} connected")
    connected=True
    while connected:
        msg=conn.recv(2048).decode('utf-8')
        if msg=="disconnect":
            connected=False
        print(f"[{Addr}] {msg}")
    conn.close()
    
        

def start():
    server.listen()
    print(f"[listning] server is listning on server {servern}")
    while True:
        conn,addr =server.accept() 
        thread=threading.Thread(target=handle_client,args=(conn,addr)) 
        thread.start()
        print(f"[total active connections] {threading.activeCount()-1} ")
        
        
        
        
print("[STARTING SERVER] server is starting...")
start()