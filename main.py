# import module
from tkinter import messagebox
from threading import Thread

from src.client import Client
from src.server import Server
from src.client_config import ClientConfigWindows
from src.host_guests_config import HostGuestsConfigWindows
from src.host_config import HostConfigWindows 
from src.guests_config import GuestsConfigWindows
from src.sender import SenderWindows

import json
import platform
import os
import time



# generate key for communication
messagebox.showinfo(title="TEME",message="Generate key for communication ( 5s ) ...")

# delete old keys
try: 
    os.mkdir("./keys")
except FileExistsError:
    messagebox.showinfo(title="TEME",message="Removing 'keys' folder ...")
    try:
        os.remove("./keys")
    except PermissionError:
        messagebox.showerror(title="TEME",message="Please delete 'keys' folder manualy")
        exit()

    os.mkdir("./keys")


# genearte new
if "Windows" in platform.platform():
    openssl_bin = "start /b bin/openssl/OpenSSL-Win64/bin/openssl.exe"

else:
    openssl_bin = "openssl"


# private
os.system(f"{openssl_bin} genpkey -algorithm RSA -out keys/private.pem")
time.sleep(5)

# public
os.system(f"{openssl_bin} rsa -pubout -in keys/private.pem -out keys/public.pem &")



# ask for client config windows
client_config_windows = ClientConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
client_config_windows.ask_config()

# setup client
client_username = client_config_windows.username
client_ip = client_config_windows.ip

client = Client(username=client_username,ip=client_ip)

# host or guests ask windows
host_guests_config_windows = HostGuestsConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
host_guests_config_windows.ask_choose()

host_guests_choose = host_guests_config_windows.choose


# open right windows for right connection role
if host_guests_choose == "host":
    # open host server config windows
    host_config_windows = HostConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
    host_config_windows.config_host()

    # run server
    host_port = host_config_windows.port 
    server = Server(host=client_ip,port=host_port)
    guests_data = server.blind_server()

    # get data
    guests_data = json.loads(guests_data)
    
    # get ip 
    guests_ip = guests_data["content"]
    
    # confirm connection
    messagebox.showinfo(title="TEME Host Config",message=f"Connection found from {guests_data["username"]}!")
    



if host_guests_choose == "guests":
    # open direct server connection windows
    guests_config_windows = GuestsConfigWindows(ico_file="icon.ico",logo_file="assets/logo.png")
    guests_config_windows.config_guests()


    # setup client for connection
    to_connect_port = guests_config_windows.port
    to_connect_ip = guests_config_windows.ip

    # send ip for etablish connection
    client.send_message(message=client.ip,server_dest=to_connect_ip,server_port=to_connect_port)
    messagebox.showinfo(title="TEME Guests Config",message="Connection to the server ...")

'''
# read local public key
with open("keys/private.pem") as public_key_file:
    public_key = public_key_file.read()
    '''


# set listener fonction 
def listener_blind(listener_host,listener_port):
    # setup server 
    server = Server(host=listener_host,port=listener_port)

    # start listener
    while True:
        data = server.blind_server()

        # get data
        data = json.loads(data)
        messagebox.showinfo(title="TEME Listener",message=str(data))


# set info for listener 
if host_guests_choose == "guests":
    listener_port = to_connect_port

if host_guests_choose == "host":
    listener_port = host_config_windows.port

listener_ip = client_ip


# run listener in background
listener_thread = Thread(target=listener_blind, args=(listener_ip,listener_port)) 
listener_thread.start()

# open sender at infinite
while True:
    sender_windows = SenderWindows(ico_file="icon.ico",logo_file="assets/logo.png")
    message = sender_windows.ask_message()


    # send message 
    if host_guests_choose == "guests":
        dest_ip = to_connect_ip
        dest_port = to_connect_port

    if host_guests_choose == "host":
        dest_ip = guests_ip
        dest_port = host_port


    client.send_message(message=message,server_dest=dest_ip,server_port=dest_port)