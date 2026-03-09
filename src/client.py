import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# Run : nc -lvnp 4444 on localhost 
server_address = ("localhost", 4444)
sock.connect(server_address)

# Trying to send something
PACKET = "Hello World!".encode("utf-8")
sock.send(PACKET)

# Close connection
sock.close()

input("Press [enter] to quit ...")