#!/usr/bin/python3

from Crypto.Hash import SHA
from Crypto import Random
from wallet import Wallet

my_wallet = Wallet("Ons Jannet")
key = my_wallet.load_keys(private_key).read()

dsize = SHA.digest_size
sentinel = Random.new().read(2048+dsize)

cipher = PKCS1_v1_5.new(key)
message = cipher.decrypt(ciphertext, sentinel)

digest = SHA.new(message[:-dsize]).digest()
if digest == message[-dsize:]:
    print("correction is correct")
    print(message)
else:
    print("encryption failed")
