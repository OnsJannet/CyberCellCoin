#!/usr/bin/python3
from datetime import datetime

class Block:
    def __init__(self, value):
        self.block = self.create_block(value)

    def create_block(self, value):
        block = {'time': str(datetime.now()),
                 'value': value}
        return block

    def dict_block(self):
        return "###\ntime{}\nvalue{}\n###".format(self.block['time'],self.block['value'])
