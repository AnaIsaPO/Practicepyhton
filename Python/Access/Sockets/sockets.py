#Request-Response cycle

#With HTTP web protocol we send and recieve data as bytes objects, instead of strings
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect('HOST', Port)
mysock.connect(('data.pr4e.org',80))
#Make a request
#We use '.encode' to send the request as UTF-8 format. Convert strings into bytes objects
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#Send it
mysock.send(cmd)

#Then we recive with a Loop while to obtain all data
while True:
    #We 're going to recieve up to 512 characters
    data = mysock.recv(512)
    #End the transmition, when we don't have more data
    if (len(data) < 1):
        break
    #We decode it. Convert of UTF-8 to unicode
    print(data.decode())
mysock.close()
