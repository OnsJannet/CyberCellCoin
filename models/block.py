#!/usr/bin/python3
from datetime import datetime

class Block:
    def __init__(self, index, value):
        self.block = self.create_block(index, value)

    def create_block(self, index, value):
        block = {'time': str(datetime.now()),
                 'value': value,
                 'index': index}
        return block

    def dict_block(self):
        return "###\ntime{}\nvalue{}\indx{}\n###".format(self.block['time'],self.block['value'],self.block['index'])

