# import module
from tkinter import *
from tkinter import PhotoImage


class HostGuestsConfigWindows():
    
    def __init__(self,ico_file,logo_file):
        self.choose = ""
        self.icon = ico_file
        self.logo = logo_file
    
    def ask_choose(self):
            
        def choose_guests():
            self.choose = "guests"
            win.destroy()
            return self.choose 
        
        def choose_host():
            self.choose = "host"
            win.destroy()
            return self.choose 
            
            
        win = Tk()
        win.iconbitmap(self.icon)
        win.title("TEME Choose Config")
        win.geometry("200x250")
        win.resizable(False,False)


        image = PhotoImage(file=self.logo)
        image_label = Label(win, image=image)
        image_label.place(x=50,y=50)

        host_button = Button(win,text="Host",command=choose_host)
        host_button.place(x=70,y=150)

        guests_button = Button(win,text="Guests",command=choose_guests)
        guests_button.place(x=65,y=175)

        win.mainloop()

