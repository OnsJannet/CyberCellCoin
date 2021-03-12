#!/usr/bin/python3
from wallet import Wallet

my_wallet = Wallet("bahlous")


my_wallet.create_keys()
my_wallet.save_keys()
my_wallet.load_keys()
pub = my_wallet.public_key
prv = my_wallet.private_key
print(pub)
a = my_wallet.user_id
print(a)