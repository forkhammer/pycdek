from .client import AbstractOrder, AbstractOrderLine, Client
VERSION = (0, 3, 1)


def get_version():
    return '.'.join(map(str, VERSION))

__version__ = get_version()

