import sys
from tkinter import *
from Constants.CommandList import CommandList


class MainFrame:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,
                             text="QUIT", fg="red",
                             command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,
                             text="Hello",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)


    def write_slogan(self):
            print(CommandList.SHOW_IMPORTANT.value)
