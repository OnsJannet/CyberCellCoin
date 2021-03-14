#!/usr/bin/python3
""" Wallet Modules that generates public private keys for each user """

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import binascii

from Crypto.Signature import PKCS1_v1_5
import Crypto.Random
from uuid import uuid4


class Wallet:

    def __init__(self, user_id):
        self.private_key = None
        self.public_key = None
        self.user_id = user_id + "-" + str(uuid4())

    def generate_RSA(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))

    def create_keys(self):
        private_key, public_key = self.generate_RSA()
        self.private_key = private_key
        self.public_key = public_key

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

    @staticmethod
    def verify_transaction(transaction):
        """
        Verify signature of transaction
        """
        public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new((str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction.signature))
    
    def sign_transaction(self, sender, recipient, amount):
        """
        Sign a transaction and return the signature
        RSA is a cryptography algorithm
        binascii.hexlify is used to convert binary data to hexadecimal representation
        """
        signer = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(self.private_key)))
        h = SHA256.new((str(sender) + str(recipient) + str(amount)).encode('utf8'))
        signature = signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')
