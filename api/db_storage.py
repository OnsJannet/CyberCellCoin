#!/usr/bin/python3
from app import mysql, session
from block import Block
from chain import Blockchain

#exceptions for transaction errors handling
class InvalidTransactionException(Exception): pass
class InsufficientFundsException(Exception): pass

class Table():
    """
    what a mysql table looks like. Simplifies access to the database 'cybercell'

    """
    def __init__(self, table_name, *args):

        self.table = table_name
        self.columns = "(%s)" %",".join(args)
        self.columnsList = args

        #if table does not already exist, create it.
        if isnewtable(table_name):
            create_data = ""
            for column in self.columnsList:
                create_data += "%s varchar(100)," %column

            cur = mysql.connection.cursor() #create the table
            cur.execute("CREATE TABLE %s(%s)" %(self.table, create_data[:len(create_data)-1]))
            cur.close()

    def getall(self):
        """
            get all the values from the table
        """

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM %s" %self.table)
        data = cur.fetchall(); return data

    def getone(self, search, value):
        """
        get one value from the table based on a column's data
        
        EXAMPLE using blockchain: ...getone("hash","00003f73gh93...")
        """
        data = {}; cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM %s WHERE %s = \"%s\"" %(self.table, search, value))
        if result > 0: data = cur.fetchone()
        cur.close(); return data

    def deleteone(self, search, value):
        """
            delete a value from the table based on column's data.
        """
        cur = mysql.connection.cursor()
        cur.execute("DELETE from %s where %s = \"%s\"" %(self.table, search, value))
        mysql.connection.commit(); cur.close()

    def deleteall(self):
        """
            delete all values from the table.
        """
        self.drop() #remove table and recreate
        self.__init__(self.table, *self.columnsList)

    def drop(self):
        """
            remove table from mysql
        """
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE %s" %self.table)
        cur.close()

    def insert(self, *args):
        """
            insert values into the table.
        """
        data = ""
        for arg in args: #convert data into string mysql format
            data += "\"%s\"," %(arg)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO %s%s VALUES(%s)" %(self.table, self.columns, data[:len(data)-1]))
        mysql.connection.commit()
        cur.close()

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
    send money from one user to another
    verify that the amount is an integer or floating value
    """
    try:
        amount = float(amount)
    except ValueError:
        raise InvalidTransactionException("Invalid Transaction.")

    #verify that the user has positive balance (exception if it is the BANK)
    if amount > get_balance(sender) or (sender == "BANK"):
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
