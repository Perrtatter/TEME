# import module
from src.client import Client
from src.server import Server





# setup client / server
client = Client(username="DEV",ip="localhost")
server = Server(host="localhost",port=4444)

# send from client
# client.send_message("First message of TEME","localhost",4444)

# run server
while True: 
    recv_data = server.blind_server()
    print(recv_data)