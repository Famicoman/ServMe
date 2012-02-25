import sys               
import socket
import string

#Make socket
srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
srvsock.bind( ("127.0.0.1", string.atoi(sys.argv[1])) )
srvsock.listen( 5 )
clisock, (remhost, remport) = srvsock.accept()

while 1:
	command = "MESSAGE HERE"+'\n'
	clisock.send(command) #Send command

clisock.close()