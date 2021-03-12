#!/usr/bin/python3
from block import Block
from hashlib import sha256

class BlockChain:

    def __init__(self):
        self.chain = [] #keeps all blocks .
        self.transactions = [] #keeps all the completed transactions in the block .
        self.nodes = set()
        self.construct_genesis() #Create the first block .


    def construct_genesis(self):
        self.construct_block(proof_nonce=0, prev_hash=0)

    def construct_block(self, proof_nonce, prev_hash):
        """
        creating new blocks in the blockchain.
        Args :
            

        """
        block = Block(
            index=len(self.chain),
            proof_nonce=proof_nonce,
            prev_hash=prev_hash,
            data=self.transactions)
        self.transactions = []

        self.chain.append(block)
        return block
    @property
    def latest_block(self):
        return self.chain[-1]

    
    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_nonce,
                                            prev_block.proof_nonce):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    def add_transaction(self, sender, recipient, amount): #New
        self.transactions.append({'sender': sender,
                                  'recipient': recipient,
                                  'amount': amount,
                                  })
        return True
    
    @staticmethod
    def proof_of_work(last_proof):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = sha256(str(new_nonce**2 - last_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        last_proof = new_nonce
        return last_proof

    @staticmethod
    def verifying_proof(last_proof, proof):
        #verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def block_mining(self, details_miner):

        self.new_data(
            sender="0",  #it implies that this node has created a new block
            receiver=details_miner,
            quantity=
            1,  #creating a new block (or identifying the proof number) is awarded with 1
        )

        last_block = self.latest_block

        last_proof_nonce = last_block.proof_nonce
        proof_nonce = self.proof_of_work(last_proof_nonce)

        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_nonce, last_hash)

        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        #obtains block object from the block data

        return Block(
            block_data['index'],
            block_data['proof_nonce'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])
