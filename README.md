# READme
Occupancy application

The codes are implemented in Python without external libs on RedHat Linux.

To execute the client-server application:
1. Download the files in /tmp folder or any other directory
2. Open three instances of linux terminal
3. Change server_ip according to your local IP in both (client and server).
4. Change client_id
5. To change occupancy data and position on the client side. Find the dataset function and change sensorData array to change the occupancy or posData to change the position as a tuple. The variable ndata should be changed if the number of data is greater than 4.
6. Save changes :)
7. Execute server.py, client0.py and client1.py separately in every terminal.
   ```
   terminal0 #python server.py
   terminal1 #python client0.py
   terminal2 #python cleint1.py
   ```
8 If you want to create more clients -> copy-paste a single client and jump to steps 3,4,5 and 6 :)

