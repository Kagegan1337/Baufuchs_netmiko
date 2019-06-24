""""
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   10.10.10.22    YES manual up                    up
GigabitEthernet0/0/1   unassigned      YES NVRAM  administratively down down
GigabitEthernet0/1/0   unassigned      YES unset  down                  down
GigabitEthernet0/1/1   unassigned      YES unset  down                  down
GigabitEthernet0/1/2   unassigned      YES unset  down                  down
GigabitEthernet0/1/3   unassigned      YES unset  down                  down
Vlan1                  unassigned      YES unset  up                    down
"""
from Model.NetmikoPort import NetmikoPort


class Parser:

    @staticmethod
    def parse_port(port):
        port = port.split(" ")
        port = [x for x in port if not x == '']
        return NetmikoPort(port[0], port[1], port[2], port[3], port[4], port[5])
