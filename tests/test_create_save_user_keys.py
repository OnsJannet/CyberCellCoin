#!/usr/bin/python3
from wallet import Wallet

my_wallet = Wallet("Abdou hidoussi")


my_wallet.create_keys()
my_wallet.save_keys()