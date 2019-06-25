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
import re

from Model.NetmikoInterface import NetmikoInterface


class Parser:

    @staticmethod
    def parse_port(port):
        port = port.replace('administratively', '')
        port = port.split(" ")
        port = [x for x in port if not x == '']
        if len(port) > 5:
            return NetmikoInterface(port[0], port[1], port[2], port[3], port[4], port[5])
        else:
            return None

    def parseVersion(self, version_string):
        first_row = version_string.split('\n')[0]
        start = first_row.find('Version')
        end = [m.start() for m in re.finditer(r",", first_row)][2]
        test = first_row[start + 8:end]

        start_number = version_string.find("Model number")
        model_string = version_string[start_number:]
        start = model_string.find(':')
        end = model_string.find('\n')
        model_string = model_string[start:end]
        print(version_string + model_string)
