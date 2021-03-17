#!/usr/bin/python3
from api.app import mysql, session
from models.engine.manage_db import *
from models.block import Block
from models.chain import Blockchain


def sql_raw(execution):
    """
    execute mysql code from python
    """
    cur = mysql.connection.cursor()
    cur.execute(execution)
    mysql.connection.commit()
    cur.close()

def isnewtable(tableName):
    """
    check if table already exists
    """
    cur = mysql.connection.cursor()

    try: #attempt to get data from table
        cur.execute("SELECT * from %s" %tableName)
        cur.close()
    except:
        return True
    else:
        return False

def isnewuser(username):
    """
    check if user already exists
    access the users table and get all values from column "username".
    """
    users = Table("users", "name", "email", "username", "password")
    data = users.getall()
    usernames = [user.get('username') for user in data]

    return False if username in usernames else True

def send_money(sender, recipient, amount):
    """
    #send money from one user to another
    verify that the amount is an integer or floating value
    """
    try:
        amount = float(amount)
    except ValueError:
        raise InvalidTransactionException("Invalid Transaction.")

    #verify that the user has positive balance (exception if it is the BANK)
    if amount > get_balance(sender) and sender != "BANK":
        raise InsufficientFundsException("Insufficient Funds.")

    #verify that the user is not sending money to themselves or amount is less than or 0
    elif sender == recipient or amount <= 0.00:
        raise InvalidTransactionException("Invalid Transaction.")

    #verify that the recipient exists
    elif isnewuser(recipient):
        raise InvalidTransactionException("User Does Not Exist.")

    #update the blockchain and sync to mysql
    blockchain = get_blockchain()
    number = len(blockchain.chain) + 1
    data = "%s==>%s==>%s" %(sender, recipient, amount)
    blockchain.mine(Block(number, data=data))
    sync_blockchain(blockchain)

def get_balance(username):
    """
    get the balance of a user.
    """
    balance = 0.00
    blockchain = get_blockchain()

    #loop through the blockchain and update balance
    for block in blockchain.chain:
        data = block.data.split("==>")
        if username == data[0]:
            balance -= float(data[2])
        elif username == data[1]:
            balance += float(data[2])
    return balance

def get_blockchain():
    """
    get the blockchain from mysql and convert to Blockchain object
    """
    blockchain = Blockchain()
    blockchain_sql = Table("blockchain", "number", "hash", "previous", "data", "nonce")
    for b in blockchain_sql.getall():
        blockchain.add(Block(int(b.get('number')), b.get('previous'), b.get('data'), int(b.get('nonce'))))

    return blockchain


def sync_blockchain(blockchain):
    """
    update blockchain in mysql table
    """
    blockchain_sql = Table("blockchain", "number", "hash", "previous", "data", "nonce")
    blockchain_sql.deleteall()

    for block in blockchain.chain:
        blockchain_sql.insert(str(block.number), block.hash(), block.previous_hash, block.data, block.nonce)
