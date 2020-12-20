import socket
import datetime



s =socket.socket() #create socket
print("Done Socket!!")

port = 6667 #port IRC

s.bind(('192.168.240.8',port)) #bind with port and IP address
print("Done Bind!! port: ", str(port))

s.listen(5) #listen connection
print("Done Listen!!")

c, addr = s.accept() #accept connection

print("Connection from: "+ str(addr)) 
c.send(b"Hi, I'm Server. Thank You!!\n") # send a data type bytes to client

buffer = c.recv(1024) #receive a data type bytes from client
print(buffer)
c.send(b"I want send the file")
buffer1= c.recv(1024)
print("Client say:",(buffer1))
i = 0
j=0
while i<2:
	if(i>=1): #receive 1 file from client to server
		file = input(str("Please rename the file:"))
		fi = open(file,'w') #create a file in same folder by input of file
		fi1 = c.recv(1024) # receive a data in bytes
		print(fi1)
		print(file)
		print(fi1)
		s = fi1.decode('UTF-8') #convert data from bytes to string
		print(s)
		fi.write(s) #write the data that receive in a file
		fi.close() #file close
		c.send(b"Server got it")
		j += 1
		if j == 1:
			break
	else: # send 1 file from server(which is text1.txt) to client
		filename = "text1.txt" #name file in same folderserver 
		f = open(filename, 'rb') #open file in bytes
		l = f.read(1024) # read file
		while(l):
			c.send(l) #send file
			print("Send",repr(l)) # show the file
			l = f.read(1024) #read file
		f.close()

		print("Done send")
		c.send(b"Thank you !")
		dat = c.recv(1024)
		print(dat)
		i += 1

while True: #chat between server and client & client only can end the connection
	buffer2 = c.recv(1024).decode()
	if not buffer2:
		break
	x =  datetime.datetime.now() #current time 
	print(x.strftime("%c")) #print current time
	print("Client say: "+str(buffer2)) 
	buffer2 = input(">>")
	c.send(buffer2.encode()) #encode the data send by client

c.close() #close the connection

