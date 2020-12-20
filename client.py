import os
import socket
import datetime
import pickle

s= socket.socket() #create soclet

port = 6667 #port IRC
s.connect(("192.168.240.8",port)) #start connection with server
print("Done connect!!")
data = s.recv(1024) 

s.send(b"Hi, I'm Client. Thank You") #send data to server
print(data)
data1=s.recv(1024) #receive data from server
s.send(b"okay") 
print("Server say:",data1)

with open("recived_file", 'wb') as f: # open and create a file named "recived_file"
	print("file opened")
	i = 0
	while (i<2):
		if(i==1): #create a file and send to server from client
			ans =input("Do you want to create a new file?") #asking create a file or not
			print (ans)
			if (ans == "y" or "Y"):
				print(ans)
				ent = input(str("Enter file name including file format:")) #create a name of file
				fh = open(ent,'w') #open file that just been create
				enter = input(str("Please write>>")) #type a string to send inside the file
				fh.write(enter) # write a string inside the file
				fh = open(ent,'rb') #open the file
				fh1 = fh.read(1024) #read the file
				while(fh1):
					s.send(fh1) #send file to server
					print("Sending to server...",repr(fh1))
					fh1 = fh.read(1024) # read the file
				data5 = s.recv(1024) #receive data from server
				print(data5)
				
				i += 1
			elif ans == "NULL" :
				fh1.close()
				fh.close()
				i += 1
			else :
				pass
				i += 1
		else: #receive from server to client
			print("receiving data.....")
			data2 = s.recv(1024) #send data to server
			print("data=%s",(data2))
			print("Received from server")
			if not data2: #if do not have a data, it will break
				break
			f.write(data2)
			data3=s.recv(1024)
			print(data3)
			s.send(b"Smile")
			i += 1
	
f.close() 
print("Success get file")
#chat between server and client (only type 'quit' from client can end the chat)
msg = input(">>")
while msg.lower().strip() != 'quit': #the chat will end if client type 'quit'
	x = datetime.datetime.now()
	print(x.strftime("%c"))
	s.send(msg.encode())
	data4= s.recv(1024).decode() #decode the data that receive
	print("Server say: "+data4)
	msg = input(">>")

s.close()
print("connection closed")




