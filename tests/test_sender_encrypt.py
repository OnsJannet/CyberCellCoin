#!/usr/bin/python3

from wallet import Wallet
from chain import BlockChain
from block import Block
#sign transaction
my_wallet = Wallet("A")
b = BlockChain()
my_wallet.create_keys()
my_wallet.save_keys()
my_wallet.load_keys()
pub = my_wallet.public_key
prv = my_wallet.private_key

verf = my_wallet.verify_transaction(b.add_transaction().data[TRANSACTION])

signer = my_wallet.sign_transaction(sender="Ons_Jannet", recipient="Aymen_Haddaji", amount=10)


print(" signature user is:", signer, verf)