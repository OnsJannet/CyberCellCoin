#!/usr/bin/python3
from wallet import Wallet

my_wallet = Wallet('Abdou hidoussi')

my_wallet.load_keys()
pub = my_wallet.public_key
prv = my_wallet.private_key
print(prv)
print("_______________________")
print(pub)
a = my_wallet.user_id
print("current user is:", a)