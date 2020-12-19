import os
import socket
import datetime
import pickle

s= socket.socket()

port = 6667
s.connect(("192.168.240.8",port))
print("Done connect!!")
data = s.recv(1024)

s.send(b"Hi, I'm Client. Thank You")
print(data)
data1=s.recv(1024)
s.send(b"okay")
print("Server say:",data1)

with open("recived_file", 'wb') as f:
	print("file opened")
	i = 0
	while i<2:
		if(i>=1):
			ans =input("Do you want to create a new file?")
			if ans == 'y' or 'Y':
				ent = input(str("Enter file name including file format:"))
				fh = open(ent,'w')
				enter = input(str("Please write>>"))
				fh.write(enter)
				fh = open(ent,'rb')
				fh1 = fh.read(1024)
				while(fh1):
					s.send(fh1)
					print("Sending to server...",repr(fh1))
					fh1 = fh.read(1024)
				data5 = s.recv(1024)
				print(data5)
				#s.send(b"Nice")
				i += 1
			else :
				i += 1
		else:
			print("receiving data.....")
			data2 = s.recv(1024)
			print("data=%s",(data2))
			print("Received from server")
			if not data2:
				break
			f.write(data2)
			data3=s.recv(1024)
			print(data3)
			i += 1
	
f.close()
print("Success get file")

msg = input(">>")
while msg.lower().strip() != 'quit':
	x = datetime.datetime.now()
	print(x.strftime("%c"))
	s.send(msg.encode())
	data4= s.recv(1024).decode()
	print("Server say: "+data4)
	msg = input(">>")

s.close()
print("connection closed")




