# import module
from src.client import Client
from src.server import Server
from src.client_config import ClientConfigWindows
from src.host_guests_config import HostGuestsConfigWindows
from src.host_config import HostConfigWindows 


# hort or guests ask windows
host_guests_config_windows = HostGuestsConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
host_guests_config_windows.ask_choose()

host_guests_choose = host_guests_config_windows.choose


# open right windows for right connection role
if host_guests_choose == "host":
    # open host server config windows
    host_config_windows = HostConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
    host_config_windows.config_host()

    # run server
    host_ip = host_config_windows.ip
    host_port = host_config_windows.port

    server = Server(host=host_ip,port=host_port)
    server.blind_server()
    

if host_guests_choose == "guests":
    # open direct server connection windows
    pass


'''# client config windows
client_config_windows = ClientConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
client_config_windows.ask_username()

client_username = client_config_windows.username

# setup client
client = Client(username=client_username,ip="localhost")'''


'''# infinte loop
while True: 
    # run server to get data
    recv_data = server.blind_server()'''
    
    