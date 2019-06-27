from tkinter import *
from tkinter import messagebox
from View.MainFrame import MainFrame


class LoginFrame:
    username_frame = None
    password_frame = None
    button_frame = None

    username_label = None
    password_label = None

    username_field = None
    password_field = None

    btn_apply = None
    btn_cancel = None

    def __init__(self):
        self.window = Tk()
        self.init_view()

    def init_view(self):
        self.window.title("Baufuchs Netmiko Login")
        self.window.geometry('400x200')

        # init frames
        self.username_frame = Frame(self.window)
        self.username_frame.pack()
        self.password_frame = Frame(self.window)
        self.password_frame.pack()
        self.button_frame = Frame(self.window)
        self.button_frame.pack()

        # Labels
        self.username_label = Label(self.username_frame, text='Admin')
        self.username_label.pack(side=LEFT)
        self.password_label = Label(self.password_frame, text='password')
        self.password_label.pack(side=LEFT)

        # Textfield
        self.username_field = Entry(self.username_frame, width=15)
        self.username_field.pack(side=RIGHT)

        self.password_field = Entry(self.password_frame, show="*", width=15)
        self.password_field.pack(side=RIGHT)

        # Buttons
        self.btn_apply = Button(self.button_frame, text="apply", command=self.apply)
        self.btn_apply.pack(side=LEFT)
        self.btn_cancel = Button(self.button_frame, text="cancel", command=self.cancel)
        self.btn_cancel.pack(side=RIGHT)

    def apply(self):
        username = self.username_field.get()
        password = self.password_field.get()
        print(username + " " + password)
        main_frame = MainFrame(username)
        main_frame.start_main_frame()

    def cancel(self):
        answer = messagebox.askyesnocancel("Close", "Anwendung wirklich beenden?")
        if answer:
            self.window.destroy()

    def start_login(self):
        self.window.mainloop()
