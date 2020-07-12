import socket

mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))

cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    text=mysocket.recv(512)
    if(len(text)<1):
        break
    print(text.decode())
mysocket.close()