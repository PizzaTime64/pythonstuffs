import socket

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM = TCP , SOCK_DGRAM = UDP

server = 'pythonprogramming.net'
port = 80
serverIP = socket.gethostbyname(server)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s.connect((server,port)) #connect to desired server and port
s.send(request.encode()) #python 3.x different, have to encode.
response = s.recv(4096)

print(response.decode())

