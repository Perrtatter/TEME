# import module
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox


class GuestsConfigWindows():
    
    def __init__(self,ico_file,logo_file):
        self.port = 0
        self.ip = ""
        self.icon = ico_file
        self.logo = logo_file
    
    def config_guests(self):
            
        def get_ip():
            self.ip = ip_entry.get()
            return self.ip 
        
        def get_port():
            self.port = port_entry.get()
            self.port = int(self.port)
            return self.port
        
        def submit():
            get_port()
            get_ip()    

            win.destroy()

        
        messagebox.showinfo(title="TEME Guests Config",message="Enter your target server ip in first input and port in second input")    
            
        win = Tk()
        win.iconbitmap(self.icon)
        win.title("TEME Guests Config")
        win.geometry("200x250")
        win.resizable(False,False)


        image = PhotoImage(file=self.logo)
        image_label = Label(win, image=image)
        image_label.place(x=50,y=50)

        ip_entry = Entry(win,width=15,bg="white",fg="black")
        ip_entry.insert(0,"Server IP")
        ip_entry.place(x=35,y=150)

        port_entry = Entry(win,width=15,bg="white",fg="black")
        port_entry.insert(0,"Port")
        port_entry.place(x=35,y=175)

        submit_button = Button(win,text="Connect",command=submit)
        submit_button.place(x=55,y=200)

        win.mainloop()

