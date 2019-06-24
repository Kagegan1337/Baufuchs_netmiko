from netmiko import ConnectHandler
from Constants.ConnectionConstants import ConnectionConstants


class Connector:
    def __init__(self, username, password):
        self.connection_params = {
            'device_type': ConnectionConstants.DEVICE_TYPE.value,
            'host': ConnectionConstants.HOSTNAME.value,
            'username': username,
            'password': password,
        }

    def establish_connection(self):
        try:
            self.net_connect = ConnectHandler(**self.connection_params)
            return True
        except:
            return False

    def show_all_interfaces(self):
        try:
            list = self.net_connect.send_command("show ip interface brief").split("\n")
            return list
        except:
            return None


