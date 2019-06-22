from NetmikoConnection.Connector import Connector


def main():
    c = Connector("test", "test")
    c.establish_connection()


if __name__ == "__main__":
    main()
