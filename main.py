# import module
from src.client import Client
from src.server import Server
from src.client_config import ClientConfigWindows
from src.host_guests_config import HostGuestsConfigWindows


# hort or guests ask windows
host_guests_config_windows = HostGuestsConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
host_guests_config_windows.ask_choose()

host_guests_choose = host_guests_config_windows.choose
print(host_guests_choose)

# client config windows

if host_guests_choose == "host":
    # open host server config windows
    pass

if host_guests_choose == "guests":
    # open direct server connection windows
    pass

client_config_windows = ClientConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
client_config_windows.ask_username()

client_username = client_config_windows.username

# setup client
client = Client(username=client_username,ip="localhost")


'''# infinte loop
while True: 
    # run server to get data
    recv_data = server.blind_server()'''
    
    