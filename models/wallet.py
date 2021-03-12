#!/usr/bin/python3
from Crypto.PublicKey import RSA
from hashlib import sha256
import binascii
import Crypto.Random
from Crypto.Signature import PKCS1_v1_5

class Wallet:

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_RSA(bits=2048):
        '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
        '''
        new_key = RSA.generate(bits, e=65537) 
        public_key = new_key.publickey().exportKey("PEM") 
        private_key = new_key.exportKey("PEM") 
        return private_key, public_key

    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet-{}.txt'.format(self.user_id), mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
                return True
            except (IOError, IndexError):
                print('Saving wallet failed...')
                return False