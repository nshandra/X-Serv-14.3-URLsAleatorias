#!/usr/bin/python3

import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))
# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

line = "HTTP/1.1 200 OK\r\n\r\n\
<html><head><meta charset='utf-8'>\
<h1>X-Serv-14.3-URLsAleatorias</h1></head>\
<body><p>Hola. Dame otra\
<a href=\"/RANDI\">\
https://localhost:1234/RANDI\
</a></p>\
</body></html>\r\n"

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        rndi = str(random.randint(0, 1000000))
        nline = line.replace('RANDI', str(rndi))
        recvSocket.send(nline.encode('utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
