import socket
import queue
import numpy as np
# *** Server params ****
server_ip="007.007.7.7"
port=8089

ndata=4  # Number of data

# *** Define the routine as a server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((server_ip, port))
serversocket.listen(5)

# *** Functions ****

    # x: position in x axis , datatype:integer from 0 to up
    # y: position in y axis , datatype:integer from 0 to up
    # sval: sensor data , datatype:binary 0: nobody or 1: there is someone
class datapckg:
    def __init__(self,idx=0,x=0,y=0,sval=0):  # Class constructor
        self.id=idx
        self.pos=(x,y)
        self.sensor=sval

def decoding(msg):
	recvdata=msg.split(",")
	print("data",recvdata)
	str0=recvdata[0].split(":")
	str1=recvdata[1].split(":")
	str2=recvdata[2].split(":")
	id=int(str0[1])
	x=int(str1[1])
	y=int(str1[2])
	sval=int(str2[1])
	#package=data(x,y,sval)
	return id,x,y,sval

def setOM():
	dp=q.get()
	(x,y)=dp.pos
	OM[x][y]=dp.sensor

def printOM():
    global ndata
    print("Printing OM")
    for i in range(ndata):
        print(OM[i])

OM = np.zeros( (4, 4) )
q=queue.Queue()

def store(dp):
	q.put(dp)

while True:
    print ("Server | Awaiting response from Client")
    connection, address = serversocket.accept()
    data = connection.recv(1024)
    msg=data.decode('utf-8')
    client_id,x,y,sval=decoding(msg)
    dp=datapckg(client_id,x,y,sval)
    #q.put(dp)
    store(dp)
    setOM()
    printOM()
    #n=data(x,y,sval)
    print("Client "+str(client_id)+": Position :",(x,y)," Sensor :",sval)
    connection.send(b"ok")
