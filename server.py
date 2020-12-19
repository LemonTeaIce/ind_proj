import socket
from io import StringIO
import datetime
import pickle


s =socket.socket()
print("Done Socket!!")

port = 6667

s.bind(('192.168.240.8',port))
print("Done Bind!! port: ", str(port))

s.listen(5)
print("Done Listen!!")

c, addr = s.accept()

print("Connection from: "+ str(addr))
c.send(b"Hi, I'm Server. Thank You!!\n")

buffer = c.recv(1024)
print(buffer)
c.send(b"I want send the file")
buffer1= c.recv(1024)
print("Client say:",(buffer1))
i = 0
j=0
while i<2:
	if(i>=1):
		file = input(str("Please rename the file:"))
		fi = open(file,'w')
		fi1 = c.recv(1024)
		print(file)
		print(fi1)
		s = fi1.decode('UTF-8')
		print(s)
		fi.write(s)
		fi.close()
		c.send(b"Server got it")
		j += 1
		if j == 1:
			break
	else:
		filename = "text1.txt"
		f = open(filename, 'rb')
		l = f.read(1024)
		while(l):
			c.send(l)
			print("Send",repr(l))
			l = f.read(1024)
		f.close()

		print("Done send")
		c.send(b"Thank you !")
		i += 1

while True:
	buffer2 = c.recv(1024).decode()
	if not buffer2:
		break
	x =  datetime.datetime.now()
	print(x.strftime("%c"))
	print("Client say: "+str(buffer2))
	buffer2 = input(">>")
	c.send(buffer2.encode())

c.close()

