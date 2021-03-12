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
print(blockchain.chain)

print("***Transaction seccessfully executed***")
print("===============================================")
print("let's execute another transaction !")
print("===============================================")

blockchain.add_transaction(
    sender="Ons_Jannet",
    recipient="Abdou_Hidoussi",
    amount=15,
)
last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_nonce, last_hash)
print(blockchain.chain)
print("***Transaction seccessfully executed***")

print("===============================================")
print("let's execute another transaction !")
print("===============================================")

blockchain.add_transaction(
    sender="Aymen_Haddaji",
    recipient="Abdou_Hidoussi",
    amount=5,
)
last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_nonce, last_hash)
print(blockchain.chain)
print("***Transaction seccessfully executed***")
print(blockchain.chain)

print("===============================================")
print("let's execute another transaction !")
print("===============================================")

blockchain.add_transaction(
    sender="Aymen_Haddaji",
    recipient="Dali_Kaouech",
    amount=20,
)
last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_nonce, last_hash)
print(blockchain.chain)
print("***Transaction seccessfully executed***")
print(blockchain.chain)

print("###############################################\n")
print("***Mining CyberCellCoin has been successful***")
print("Blockchain Records Status :")
print(blockchain.chain)