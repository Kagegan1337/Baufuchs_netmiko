from netmiko import ConnectHandler
from Constants.ConnectionConstants import ConnectionConstants
from Constants.CommandList import CommandList


class ConnectionController:
    net_connect = None

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
            return self.net_connect.send_command(CommandList.SHOW_INTERFACE).split("\n")
        except:
            return None

    def show_interface(self, netmiko_interface):
        print(CommandList.SHOW_INTERFACE.value + " " + netmiko_interface.get_name())
        self.net_connect.send_command(CommandList.SHOW_INTERFACE.value + " " + netmiko_interface.get_name())

    def show_current_config(self, netmiko_interface):
        self.net_connect.send_command("show running-config interface " + netmiko_interface.get_name())

    def send_config(self, config):
        self.net_connect.send_config_set(config)

    def create_config(self, interface, config_string):
        return [interface.get_name(), config_string]

    def get_version(self):
        # parse
        self.net_connect.send_command(CommandList.SHOW_VERSION.value)
        return -1

    def get_uptime(self):
        # parse
        self.net_connect.send_command(CommandList.UPTIME.value)
        return -1
