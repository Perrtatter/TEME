from tkinter import *


class TestSender():

    def __init__(self):
        self.mess = ""

    def ask_message(self):

        def get_message():
            self.mess = test_entry.get()
            win.destroy()
            return self.mess

        win = Tk()
        test_entry = Entry(win)
        test_entry.pack()

        test_button = Button(win,text="Send",command=get_message)
        test_button.pack()

        win.mainloop()


# while True is not so good :/
while True:
    test_sender = TestSender()
    test_sender.ask_message()

    message = test_sender.mess

    print(message)