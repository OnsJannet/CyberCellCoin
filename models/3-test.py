#!/usr/bin/python3
from wallet import Wallet

my_wallet = Wallet("bahlous")


my_wallet.create_keys()
my_wallet.save_keys()