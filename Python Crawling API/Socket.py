import socket
# Create an INET, STREAMing socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connect to the web server on port 80 - the normal http port
mysock.connect( ('data.pr4e.org', 80) )

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # Turn from unicode to byte
mysock.send(cmd) # Used to send data from one socket to another socket

while True:
    data = mysock.recv(512) # Recieve data in 512 bytes
    if (len(data) < 1):
        break
    print(data.decode()) # Decode data into a unicode string
mysock.close() # Close socket when connection is lost