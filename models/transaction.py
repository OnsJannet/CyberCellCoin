#!/usr/bin/python3
""" Transactions """
from datetime import datetime


class Transaction:
    """
        Represents the transactions where
        sender is the the senders public key
        recipient is the recipients public key
        amount is the amount of coins sent
        time is the time of the transaction
    """

    def __init__(self, sender, recipient, amount, history):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.time = str(datetime.now())
        self.history = history
        self.history.append({
            'From': self.sender,
            'To': self.recipient,
            'Amount': self.amount,
            'Date': self.time
            })

    def dict_transaction(self):
        return "###{}###{}###{}###{}###{}###".format(
            self.sender,
            self.recipient,
            self.amount,
            self.time,
            self.history)
