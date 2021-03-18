#!/usr/bin/python3
from chain import Blockchain, Block
def main():
    blockchain = Blockchain()
    database = ["hello", "goodbye", "test", "DATA here", "test2"]

    num = 0

    for data in database:
        num += 1
        blockchain.mine(Block(num, data=data))

    for block in blockchain.chain:
        print(block)

    print(blockchain.isValid())
    # i try to change data in blck number 2 without valid nonce
    blockchain.chain[2].data = "NEW DATA"
    blockchain.mine(blockchain.chain[2])
    print(blockchain.isValid())


if __name__ == '__main__':
    main()
