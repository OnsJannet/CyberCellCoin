#!/usr/bin/python3
""" Transactions """
from datetime import datetime


class pending_transaction:
    """
        Represents the yet to be accepted
        transactions
    """

    def __init__(self, pending_transaction):
        self.pending_transaction = []


class new_transaction:

    """
        Represents the transactions where
        sender is the the sender’s public key
        recipient is the recipient’s public key
        amount is the amount of coins sent
        time is the time of the transaction
    """

    def __init__(self, sender, recipient, amount, time):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.time = str(datetime.now())
        self.pending_transaction.append()
        return self.prev['index'] + 1
