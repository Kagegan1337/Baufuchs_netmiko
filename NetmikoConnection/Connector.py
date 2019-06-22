from netmiko import ConnectHandler
from Constants import ConnectionConstants


class Connector:
    def __init__(self, username, password):
        self.connection_params = {
            'device_type': ConnectionConstants.DEVICE_TYPE,
            'host': ConnectionConstants.HOSTNAME,
            'username': username,
            'password': password,
        }
        #self.net_connect = ConnectHandler(**self.connection_params)

    def establish_connection(self):
        print(self.connection_params.values())

