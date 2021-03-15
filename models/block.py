#!/usr/bin/python3
from datetime import datetime
from hashlib import sha256


class Block:

    def __init__(self, index, proof_nonce, prev_hash, data, wallets, timestamp=None):
        """ 
            Args :
            self :  refers to the instance of the Block class,\
                    making it possible to access the methods and attributes\
                    associated with the class .
            index : 
                    keeps track of the position of the block within the blockchain .
            proof_nonce :
                    the number produced during the creation of a new block (Mining) .
            prev_hash :
                    refers to the hash of the previous block within the chain .
            data :
                    gives a record of all transactions completed (Ledger) .
            timestamp :
                    put a timestamp for the transactions .
            """
        
        self.index = index
        self.proof_nonce = proof_nonce
        self.prev_hash = prev_hash
        self.data = {'Transaction':data , 'Wallets':wallets}
        self.timestamp = str(datetime.now())


    @property
    def calculate_hash(self):
        """
        generate the hash of the blocks using the above values with the SHA-256 module .
        """
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_nonce,
                                              self.prev_hash, self.data,
                                              self.timestamp)

        return sha256(block_of_string.encode()).hexdigest()



        return True

    def __repr__(self):
        return "Index : {}\n - Nonce : {}\n - Previous Hash : {}\n - TRANSACTION : {}\n - Time : {}\n".format(self.index, self.proof_nonce,
                                               self.prev_hash, self.data,
                                               self.timestamp)
