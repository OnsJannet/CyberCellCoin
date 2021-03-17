#!/usr/bin/python3
""" Hash Module that crypt and encode data """

import json
from hashlib import sha256


class Hash:

    """ Method that hash data and return encoded hashed block"""

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return sha256(encoded_block).hexdigest()
