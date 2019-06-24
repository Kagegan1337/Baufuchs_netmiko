
from NetmikoConnection.Connector import Connector
from tkinter import *
from View.MainFrame import MainFrame
from Parser.NetmikoParser import Parser


def main():
    #c = Connector("jokapuser", "jokap123")
    #c.establish_connection()
    #c.show_all_interfaces()
    p = Parser()
    p.parse_port("GigabitEthernet0/0/0   10.10.10.22    YES manual up                    up")

if __name__ == "__main__":
    main()
