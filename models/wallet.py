#!/usr/bin/python3
""" Wallet Modules that generates public private keys for each user """

from Crypto.PublicKey import RSA
from hashlib import sha256
import binascii
import secrets
from Crypto.Signature import PKCS1_v1_5


class Wallet:

    def __init__(self, user_id):
        self.private_key = None
        self.public_key = None
        self.user_id = user_id

    def generate_RSA(self, bits=2048):
        '''
        Generate an RSA keypair with an exponent of 65537 in PEM format
        param: bits The key length in bits
        Return private key and public key
        '''
        new_key = RSA.generate(bits, e=secrets.randbelow(2048))
        self.public_key = new_key.publickey().exportKey("PEM")
        self.private_key = new_key.exportKey("PEM")
        return self.private_key, self.public_key

    def create_keys(self):
        private_key, public_key = self.generate_RSA()
        self.private_key = private_key
        self.public_key = public_key

    def save_keys(self):
        if self.public_key is not None and self.private_key is not None:
            try:
                with open('wallet-{}.txt'.format(self.user_id), mode='wb') as f:
                    f.write(self.public_key)
                    f.write(bytes('\n', 'utf-8'))
                    f.write(self.private_key)
                return True
            except (IOError, IndexError):
                print('Saving wallet failed...')
                return False

    def load_keys(self):
        try:
            with open('wallet-{}.txt'.format(self.user_id), mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
            return True
        except (IOError, IndexError):
            print('Loading wallet failed...')
            return False
