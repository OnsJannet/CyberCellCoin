#!/usr/bin/python3
from datetime import datetime

class Block:
    def __init__(self, value, history):
        self.history = history
        self.history.append(value)
        self.block = self.create_block(value)

    def create_block(self, value):
        block = {'time': str(datetime.now()),
                 'value': value,
                 'history': self.history}
        return block

