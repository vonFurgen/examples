import socket
import time
# *** Client params ***
server_ip = "007.007.7.7"  # It defines the server IP assigned by the router
port = 8089     # It defines the port used by the server
client_id=1     # It defines the client ID

# *** Application variables
ndata=4         # Total number of datasets          # Global var
timeinterval=5  # Time interval [seconds] , datatype:integer
class pckg:
    # x: position in x axis , pckgtype:integer from 0 to up
    # y: position in y axis , datatype:integer from 0 to up
    # sval: sensor data , datatype:binary 0: nobody or 1: there is someone
    def __init__(self,client_id,x,y,sval):  # Class constructor
        self.id=client_id
        self.pos=(x,y)
        self.sensor=sval

#def sendData(data d):

def datasets():
    sensorData=[1,1,0,0]
    posData=[(2,1),(2,2),(3,1),(3,2)]
    datapackage=[]
    for i in range(ndata):
        x,y=posData[i]
        datapackage.append(pckg(client_id,x,y,sensorData[i]))
    return datapackage



# *** This function emulates the reading of sensor devices
def emulator():
    global arr,tick
    time.sleep(timeinterval)
    data=arr[tick]
    tick+=1
    return data

def protocol(pckg):
    # The client sends the datapackage according with the following structure
    # cid:val0,pos:x:y,sen:val1
    client_id=pckg.id
    x,y=pckg.pos
    sval=pckg.sensor
    msg="cid:"+str(client_id)+",pos:"+str(x)+":"+str(y)+",sensor:"+str(sval)
    print("Sending msg > "+msg)
    return msg

tick=0
arr=datasets()
#print(arr[0].pos)
#{[1, 2], 0}; {[1, 3], 1}; {[2, 2], 0}; {[2, 3], 0}

while(tick<=(ndata-1)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        package=protocol(emulator())
        #s.sendall(package)
        s.sendall(bytes(package, 'utf-8'))
        data = s.recv(1024)
        print(f"Server said > {data!r}")
