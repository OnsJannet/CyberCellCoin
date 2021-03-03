#!/usr/bin/python3
""" Basic Block """
from datetime import datetime

class Block:
    def __init__(self, value, prev):
        self.block = self.create_block(value, prev)

    def create_block(self, value, prev):
        block = {'time': str(datetime.now()),
                 'value': value,
                 'perv': prev}
        return block

    def dict_block(self):
        return self.block
