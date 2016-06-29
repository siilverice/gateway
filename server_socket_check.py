import socket
import os
import subprocess

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('161.246.70.75', 8023))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    try:
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            print buf
	    # os.system(buf)
	    list = buf.split()
	    try:
		# subprocess.check_call(list)
		p = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		result, err = p.communicate()
		if 'error' in result:
		    print "error"
		    connection.send("1") #fail
		else:
		    print "success"
		    connection.send("0") #success
	    except:
		connection.send("1") #fail
    
    except KeyboardInterrupt:
	print "close socket"
	break

serversocket.close() 
