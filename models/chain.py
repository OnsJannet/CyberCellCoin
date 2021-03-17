#!/usr/bin/python3
<<<<<<< HEAD
"""The "LinkedList" of the blocks-- a chain of blocks"""

from hashlib import sha256
from models.block import Block

#to use sha256 hash for the blockchain


class Blockchain():
    """the number of zeros in front of each hash"""
    difficulty = 4

    def __init__(self):
        """
        restarts a new blockchain or the existing one upon initialization
        """
        self.chain = []


    def add(self, block):
        """
        add a new block to the chain
        """
        self.chain.append(block)

    def remove(self, block):
        """
        remove a block from the chain
        """
        self.chain.remove(block)

    
    def mine(self, block):
        """
        find the nonce of the block that satisfies the difficulty and add to chain.
        attempt to get the hash of the previous block.
        this should raise an IndexError if this is the first block.
        """
        try: block.previous_hash = self.chain[-1].hash()
        except IndexError: pass

        #loop until nonce that satisifeis difficulty is found
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                #increase the nonce by one and try again
                block.nonce += 1

    def isValid(self):
        """
        check if blockchain is valid
        loop through blockchain
        """
        for i in range(1,len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            #compare the previous hash to the actual hash of the previous block
            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                return False

        return True
=======
from block import Block
from hash import Hash

class Chain:
    def __init__(self):
        self.code = Hash()
        self.chain = []
        save = {'prev':None,
                'index':0,
                'block':"First of his name"}
        self.chain.append(save)
    
    def add_block(self, block):
        save = {'prev': self.code.hash(self.chain[-1]['block']),
                'index':self.chain[-1]['index'] + 1,
                'block':block.__dict__}
        self.chain.append(save)

    def dict_chain(self):
        return self.chain

>>>>>>> Front_OJ
