#!/usr/bin/python3
from wallet import Wallet

my_wallet = Wallet()

my_wallet.generate_RSA()
my_wallet.save_keys()
