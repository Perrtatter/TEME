# import module
from tkinter import *
from tkinter import PhotoImage


class ClientConfigWindows():
    
    def __init__(self,ico_file,logo_file):
        self.username = ""
        self.icon = ico_file
        self.logo = logo_file
    
    def ask_username(self):
            
        def get_username():
            self.username = username_entry.get()
            win.destroy()
            return self.username 
            
            
        win = Tk()
        win.iconbitmap(self.icon)
        win.title("TEME Client Config")
        win.geometry("200x250")
        win.resizable(False,False)


        image = PhotoImage(file=self.logo)
        image_label = Label(win, image=image)
        image_label.place(x=50,y=50)


        username_entry = Entry(win,width=15,bg="white",fg="black")
        username_entry.place(x=35,y=100)

        sender_button = Button(win,text="Set username",command=get_username)
        sender_button.place(x=50,y=150)

        win.mainloop()

