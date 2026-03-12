# import module
from src.client import Client
from src.server import Server
from src.client_config import ClientConfigWindows


# client config windows
client_config_windows = ClientConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
client_config_windows.ask_username()

client_username = client_config_windows.username

# setup client
client = Client(username=client_username,ip="localhost")


'''# infinte loop
while True: 
    # run server to get data
    recv_data = server.blind_server()'''
    
    