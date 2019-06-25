
from NetmikoConnection.ConnectionController import ConnectionController
from tkinter import *
from View.MainFrame import MainFrame
from Parser.NetmikoParser import Parser


def main():
    c = ConnectionController("jokapuser", "jokap123")
    p = Parser()
    list = []
    print(c.establish_connection())
    p.parseVersion(c.get_version())


if __name__ == "__main__":
    main()
