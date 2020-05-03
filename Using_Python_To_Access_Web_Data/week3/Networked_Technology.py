import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))

cmd='GET http://data.pr4e.org/words.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
# <html><head>
# <title>404 Not Found</title> 
# </head><body>
# <h1>Not Found</h1>
# <p>The requested URL /word.txt was not found on this server.</p>
# <hr>
# <address>Apache/2.4.18 (Ubuntu) Server at data.pr4e.org Port 80</address>
# </body></html>

while True:
    data=mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()



#### Same as doing : telnet data.pr4e.org 80