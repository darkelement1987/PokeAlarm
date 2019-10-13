import os
import binascii

# Global variables used by all functions
config = {
    'ROOT_PATH': os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
}

not_so_secret_url = binascii.unhexlify(
    '68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f776869746577696c6c656d2f506f676f4173736574732f726573697a65642f6e6f5f626f726465722f')


class Unknown:
    """ Enum for unknown DTS. """
    TINY = '?'
    SMALL = '???'
    REGULAR = 'unknown'
    EMPTY = ''

    __unknown_set = {TINY, SMALL, REGULAR}

    @classmethod
    def is_(cls, *args):
        """ Returns true if any given arguments are unknown, else false """
        for arg in args:
            if arg in cls.__unknown_set:
                return True
        return False

    @classmethod
    def is_not(cls, *args):
        """ Returns false if any given arguments are unknown, else true """
        for arg in args:
            if arg in cls.__unknown_set:
                return False
        return True

    @classmethod
    def or_empty(cls, val, default=EMPTY):
        """ Returns an default if unknown, else the original value. """
        return val if val not in cls.__unknown_set else default
