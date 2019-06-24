"""
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   10.10.10.22    YES manual up                    up
GigabitEthernet0/0/1   unassigned      YES NVRAM  administratively down down
GigabitEthernet0/1/0   unassigned      YES unset  down                  down
GigabitEthernet0/1/1   unassigned      YES unset  down                  down
GigabitEthernet0/1/2   unassigned      YES unset  down                  down
GigabitEthernet0/1/3   unassigned      YES unset  down                  down
Vlan1                  unassigned      YES unset  up                    down
"""


class NetmikoPort:

    def __init__(self, name, ip_address, health, method, status, protocol):
        self.name = name
        self.ip_address = ip_address
        self.health = health
        self.method = method
        self.status = status
        self.protocol = protocol

    def get_name(self):
        return self.name

    def get_ip_address(self):
        return self.ip_address

    def get_health(self):
        return self.health

    def get_method(self):
        return self.method

    def get_status(self):
        return self.status

    def get_protocol(self):
        return self.protocol

    def set_name(self, name):
        self.name = name

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def set_health(self, health):
        self.health = health

    def set_method(self, mehtod):
        self.method = mehtod

    def set_status(self, status):
        self.status = status

    def set_protocol(self, protocol):
        self.protocol = protocol
