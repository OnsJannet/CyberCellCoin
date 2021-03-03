#!/usr/bin/python3
from block import Block

class Chain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        if(self.chain == []):
            save = {'prev':None, 'block':block}
            self.chain.append(save)
        else:
            save = {'prev':self.chain[-1]['block'].block['index'], 'block':block}
            self.chain.append(save)

    def dict_chain(self):
        return self.chain

