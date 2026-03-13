# import module
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox


class HostConfigWindows():
    
    def __init__(self,ico_file,logo_file):
        self.port = 0
        self.ip = ""
        self.icon = ico_file
        self.logo = logo_file
    
    def config_host(self):
            
        def get_port():
            self.port = port_entry.get()
            self.port = int(self.port)

            messagebox.showinfo(title="TEME Host Config",message="Server running, waiting for guests connection ...")    

            win.destroy()
            return self.port 

            

        
        messagebox.showinfo(title="TEME Host Config",message="Enter your local ip in first input and port in second input")    
            
        win = Tk()
        win.iconbitmap(self.icon)
        win.title("TEME Host Config")
        win.geometry("200x250")
        win.resizable(False,False)


        image = PhotoImage(file=self.logo)
        image_label = Label(win, image=image)
        image_label.place(x=50,y=50)


        port_entry = Entry(win,width=15,bg="white",fg="black")
        port_entry.insert(0,"Port")
        port_entry.place(x=35,y=150)

        submit_button = Button(win,text="Start",command=get_port)
        submit_button.place(x=65,y=175)

        win.mainloop()

