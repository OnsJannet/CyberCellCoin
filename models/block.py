#!/usr/bin/python3
""" The "node" of the blockchain. Points to the previous block\
         by its unique hash in previous_hash. """


from hashlib import sha256
from datetime import datetime

"""Takes in any number of arguments and produces a sha256 hash as a result"""
def updatehash(*args):
        
    hashing_text = ""
    h = sha256()

    #loop through each argument and hash
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class Block():
    """
    default data for block defined in constructor. Minimum specified should be number and data.
    """
    def __init__(self, number=0, previous_hash="0"*64, data=None, nonce=0, timestamp=None):
        self.data = data
        self.number = number
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = str(datetime.now())

    #returns a sha256 hash for the block's data. Function instead of variable in constructor
    #to avoid corruption of the variable.
    def hash(self):
        return updatehash(
            self.number,
            self.previous_hash,
            self.data,
            self.nonce,
            self.timestamp
        )

    def __str__(self):
        """
        returns a string of the block's data. Useful for diagnostic print statements.
        """
        return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n Time: %s" %(
            self.number,
            self.hash(),
            self.previous_hash,
            self.data,
            self.nonce,
            self.timestamp
            )
        )
