from enum import Enum


class CommandList(Enum):
    SHOW_VERSION = 'show version'

    SHOW_INTERFACE = 'show interface'

    ENABLE = 'no shutdown'

    DISABLE = 'shutdown'

    SHOW_ALL = 'show ip interface'

    SHOW_IMPORTANT = 'show ip interface brief'
