#!/usr/bin/python3

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from wallet import Wallet

my_wallet = Wallet("Ons Jannet")
message = "hello holberton to be encrypted"
message.encode('utf-8').SHA.new(message)
key = my_wallet.load_keys(public_key).read()
cipher = PKCS2_v1_5.new(key)
ciphertext = cipher.encrypt(message+h.digest())
