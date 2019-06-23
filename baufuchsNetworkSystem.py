import sys

from PyQt5.QtWidgets import QApplication

from NetmikoConnection.Connector import Connector
from View.MainFrame import MainFrame


def main():
    c = Connector("test", "test")
    c.establish_connection()

    app = QApplication(sys.argv)
    mF = MainFrame()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
