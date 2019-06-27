from tkinter import *


class MainFrame:

    def __init__(self, username):
        self.username = username
        self.window = Tk()
        self.init_view()

    def init_view(self):
        buttons = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.window.title("Interfaces")
        self.window.geometry("800x600")

        login_frame = Frame(self.window)
        login_frame.pack()
        button_frame = Frame(self.window)
        button_frame.pack(side=LEFT)

        username_label = Label(login_frame, text=self.username)
        username_label.pack(side=LEFT)

        scrollbar = Scrollbar(button_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        col = 0
        for s in buttons:
            simple_btn_frame = Frame(button_frame)
            button = Button(simple_btn_frame, text=s)
            button.pack()
            simple_btn_frame.grid(row=0, column=col)
            col += 1

    def start_main_frame(self):
        self.window.mainloop()

    def end_main_frame(self):
        self.window.destroy()
