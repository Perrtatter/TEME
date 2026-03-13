# import module
from tkinter import *
from tkinter import PhotoImage


class SenderWindows():
    
    def __init__(self,ico_file,logo_file):
        self.message = ""
        self.icon = ico_file
        self.logo = logo_file
    
    def ask_message(self):
            
        def get_message():
            self.message = message_entry.get()
            win.destroy()
            return self.message 
            
            
        win = Tk()
        win.iconbitmap(self.icon)
        win.title("TEME Sender")
        win.geometry("200x250")
        win.resizable(False,False)


        image = PhotoImage(file=self.logo)
        image_label = Label(win, image=image)
        image_label.place(x=50,y=50)


        message_entry = Entry(win,width=15,bg="white",fg="black")
        message_entry.insert(0,"Message")
        message_entry.place(x=35,y=100)

        sender_button = Button(win,text="Send message",command=get_message)
        sender_button.place(x=50,y=150)

        win.mainloop()

