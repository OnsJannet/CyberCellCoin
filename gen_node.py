#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, send_file, request, jsonify
import requests
import json
import copy
from models.wallet import Wallet
from models.chain import BlockChain
from models.block import Block
from uuid import uuid4


app = Flask(__name__)


CyberCellCoin = BlockChain()
CyberCellCoin.nodes = ["http://0.0.0.0:8000/"]
gen_block = Block(transaction=[], wallets={})
CyberCellCoin.add(gen_block)

@app.route('/chain', strict_slashes=False)
def chain():
    ls = []
    for index in range(len(CyberCellCoin.chain)):
        ls.append(CyberCellCoin.chain[index].__dict__)
    return jsonify(ls)

@app.route('/peers', strict_slashes=False)
def peers():
    return jsonify(CyberCellCoin.nodes)


@app.route('/block', methods=['POST'])
def recive_block():
    block = request.json
    recived = Block()
    recived.__dict__ = block
    print("Block has been recived")
    CyberCellCoin.add(recived)
    return request.json

@app.route('/ping', methods=['POST'])
def recive_peers():
    recived = request.json
    print("Peer has been recived")
    if (not (recived in CyberCellCoin.nodes)):
        CyberCellCoin.nodes.append(recived)
    return request.json

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
