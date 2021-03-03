#!/usr/bin/python3
from block import Block

class Chain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        if(self.chain == []):
            save = {'prev':None, 'index':1, 'block':block}
            self.chain.append(save)
        else:
            save = {'prev':self.chain[-1]['index'], 'index':self.chain[-1]['index'] + 1, 'block':block}
            self.chain.append(save)

    def dict_chain(self):
        return self.chain
