#!/usr/bin/python3
from block import Block
from chain import BlockChain

blockchain = BlockChain()

print("Blockchain Records Status :")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_nonce = last_block.proof_nonce
proof_nonce = blockchain.proof_of_work(last_proof_nonce)
print("***Mining CyberCellCoin about to start***")

blockchain.add_transaction(
    sender="Ons_Jannet",  #it implies that this node has created a new block
    recipient="Aymen_Haddaji",  #let's send Aymen some coins!
    amount=10,  #creating a new block (or identifying the proof number) is awarded with 10
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_nonce, last_hash)
print(blockchain.chain, blockchain.transactions, blockchain.nodes)