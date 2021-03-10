#!/usr/bin/python3
""" Transactions """
from datetime import datetime
import json


class Transaction:
    """
        Represents the transactions where
        sender is the the senders public key
        recipient is the recipients public key
        amount is the amount of coins sent
        time is the time of the transaction
    """

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.time = str(datetime.now())

    def dict_transaction(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True)
