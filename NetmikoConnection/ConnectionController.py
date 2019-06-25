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

    def get_all_interfaces(self):
        try:
            return self.net_connect.send_command(CommandList.SHOW_IMPORTANT.value).split("\n")
        except:
            return None

    def show_interface(self, netmiko_interface):
        return self.net_connect.send_command(CommandList.SHOW_INTERFACE.value + " " + netmiko_interface.get_name())

    def show_current_config(self, netmiko_interface):
        return self.net_connect.send_command("show running-config interface " + netmiko_interface.get_name())

    def send_config(self, config):
        self.net_connect.send_config_set(config)

    def create_config(self, interface, config_string):
        return [interface.get_name(), config_string]

    def get_version(self):
        # parse
        return self.net_connect.send_command(CommandList.SHOW_VERSION.value)


    def create_vlan(self, number):
        config_command = ['vlan ' + str(number), 'jokap vlan ' + str(number)]
        self.net_connect.send_config_set(config_command)

    def delete_vlan(self, number):
        config_command = ['no vlan ' + str(number)]
        self.net_connect.send_config_set(config_command)

    def show_vlan(self):
        return self.net_connect.send_command(CommandList.SHOW_VLAN.value)

    def change_vlan(self, interface, vlan):
        config_command = ['int ' + interface.get_name(), 'switchport mode access',
                          'switchport access vlan ' + str(vlan)]
        return self.net_connect.send_config_set(config_command)

    def port_toggle_status(self, interface):
        config_command = ['interface ' + interface.get_name()]
        if interface.get_status() == 'down':
            config_command.append('no shutdown')
        else:
            config_command.append('shutdown')
        self.net_connect.send_config_set(config_command)

    def port_get_stauts(self, port):
        return self.net_connect.send_command(CommandList.SHOW_INTERFACE.value + " " + port.get_name() + " status")
