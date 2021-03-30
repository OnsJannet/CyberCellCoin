#!/usr/bin/python3
""" Module to handle all the transactions process """
from wallet import Wallet
from datetime import datetime

class Transaction:
    def __init__(self, sender, recipient, amount):
        """
        Creates a new transaction
        :param sender: <str> sender account
        :param recipient: <str> recipient account
        :param amount: <float> amount to be transferred
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount


    def validate(self):
        """
        Checks if a transaction is valid
        :return: <bool> True if it is valid, False if not.
        """

        # Prevent stealing by creating negative transactions
        if self.amount < 0:
            return False

        return True

    def to_dict(self):
        return ([('sender', self.sender.user_id), ('recipient', self.recipient.user_id), ('amount', self.amount)])
