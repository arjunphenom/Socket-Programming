import socket
port=5050
servern=socket.gethostbyname(socket.gethostname())
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addrr=(servern,port)
client.connect(addrr)

