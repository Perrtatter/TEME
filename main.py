# import module
from tkinter import *
from tkinter import PhotoImage

from src.client import Client
from src.server import Server



# setup client / server
client = Client(username="DEV",ip="localhost")
server = Server(host="localhost",port=4444) 


# windows config
win = Tk()
win.iconbitmap("icon.ico")
win.title("TEME Client")
win.geometry("200x200")
win.resizable(False,False)

# Load the logo 
image = PhotoImage(file="logo.png")
image_label = Label(win, image=image)
image_label.pack()

# run listener button
listener_button = Button(win,text="Listener")
listener_button.pack()

# run sender button
sender_button = Button(win,text="Sender")
sender_button.pack()

win.mainloop()

# send from client
# client.send_message("First message of TEME","localhost",4444)


'''# infinte loop
while True: 
    # run server to get data
    recv_data = server.blind_server()'''
    
    