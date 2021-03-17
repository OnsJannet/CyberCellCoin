#!/usr/bin/python3
from app import mysql, session
from models.block import Block
from models.chain import Blockchain
from models.engine.db_storage import Db_storge

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
