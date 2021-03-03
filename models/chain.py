#!/usr/bin/python3
from block import Block
from hash import Hash

class Chain:
    def __init__(self):
        self.code = Hash()
        self.chain = []
        self.new_hash = None

    def add_block(self, block):
        if(self.chain == []):
            save = {'prev':None,
                    'index':0,
                    'block':"First of his name"}
            self.chain.append(save)

            save = {'prev': self.code.hash(self.chain[-1]['block']),
                    'index':self.chain[-1]['index'] + 1,
                    'block':block.__dict__}
            self.chain.append(save)
        else:
            save = {'prev': self.code.hash(self.chain[-1]['block']),
                    'index':self.chain[-1]['index'] + 1,
                    'block':block.__dict__}
            self.chain.append(save)

    def dict_chain(self):
        return self.chain


