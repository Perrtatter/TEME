# import module
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

class ClientConfigWindows():
    
    def __init__(self,ico_file,logo_file):
        self.username = ""
        self.ip = ""
        self.icon = ico_file
        self.logo = logo_file
    
    def ask_config(self):
            
        def get_username():
            self.username = username_entry.get()
            return self.username 
    
        def get_ip():
            self.ip = ip_entry.get()
            return self.ip
        
        def submit():
            get_username()
            get_ip()
            win.destroy()


        messagebox.showinfo(title="TEME Client Config",message="Enter your username in first input and local ip in second input") 

        win = Tk()
        win.iconbitmap(self.icon)
        win.title("TEME Client Config")
        win.geometry("200x250")
        win.resizable(False,False)


        image = PhotoImage(file=self.logo)
        image_label = Label(win, image=image)
        image_label.place(x=50,y=50)


        username_entry = Entry(win,width=15,bg="white",fg="black")
        username_entry.insert(0,"Username")
        username_entry.place(x=35,y=120)

        ip_entry = Entry(win,width=15,bg="white",fg="black")
        ip_entry.insert(0,"Local IP")
        ip_entry.place(x=35,y=140)

        sender_button = Button(win,text="Set client",command=submit)
        sender_button.place(x=50,y=175)

        win.mainloop()