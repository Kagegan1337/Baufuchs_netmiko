
from NetmikoConnection.ConnectionController import ConnectionController
from tkinter import *
from View.MainFrame import MainFrame
from Parser.NetmikoParser import Parser


def main():
    c = ConnectionController("jokapuser", "jokap123")
    p = Parser()
    interface = p.parse_port("GigabitEthernet0/0/0   10.10.10.22    YES manual up                    up")
    c.show_interface(interface)


if __name__ == "__main__":
    main()
