#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, send_file, request, jsonify
import requests
import json
import copy
from models.wallet import Wallet
from models.chain import Blockchain
from models.block import Block
from uuid import uuid4


app = Flask(__name__)




def sync_chain(address):
    req = requests.get(address)
    global CyberCellCoin
    CyberCellCoin = Blockchain()
    CyberCellCoin.nodes = ["http://0.0.0.0:8000/res"]
    recived = req.json()
    CyberCellCoin.chain =  []
    empty = Block()
    for index in range(len(recived)):
        new = copy.copy(empty)
        new.__dict__ = recived[index]
        CyberCellCoin.add(new)

def sync_nodes(address):
    req = requests.get(address)
    CyberCellCoin.nodes = req.json()


@app.route('/chain', strict_slashes=False)
def chain():
    ls = []
    for index in range(len(CyberCellCoin.chain)):
        ls.append(CyberCellCoin.chain[index].__dict__)
    return jsonify(ls)

@app.route('/peers', strict_slashes=False)
def peers():
    return jsonify(CyberCellCoin.nodes)

@app.route('/wallet/<user_id>', methods=['POST'])
def wallet_create(user_id):
    user_id = user_id + "-" + str(uuid4())
    wallets = CyberCellCoin.latest_block.data["wallets"].copy()
    wallets[user_id] = {"user_id": user_id, "balance": 0}
    old_transaction = CyberCellCoin.latest_block.data["transaction"].copy()
    data = {"transaction": old_transaction, "wallets": wallets}
    new = Block(data=data)
    CyberCellCoin.add(new)

    for index in range(len(CyberCellCoin.nodes)):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        url = CyberCellCoin.nodes[index]
        url = url + "block"
        data = CyberCellCoin.latest_block.__dict__
        requests.post(url, json=data, headers=headers)

    for index in range(len(CyberCellCoin.nodes)):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        url = CyberCellCoin.nodes[index]
        url = url + "ping"
        data = request.url_root
        requests.post(url, json=data, headers=headers)

    print(not (request.url_root in CyberCellCoin.nodes))
    if (not (request.url_root in CyberCellCoin.nodes)):
        CyberCellCoin.nodes.append(request.url_root)

    return user_id


@app.route('/ter/<sender_id>/<reciver_id>/<ammount>', methods=['POST'])
def transaction_create(sender_id,reciver_id,ammount):
    user_id = sender_id + "-" + str(uuid4())
    transaction = {"From": sender_id,"To": reciver_id,"Ammount": ammount,"Time": "tawa"}
    new_transaction = CyberCellCoin.latest_block.data["transaction"].copy()
    new_transaction.append(transaction)
    old_wallets = CyberCellCoin.latest_block.data["wallets"].copy()
    data = {"transaction": new_transaction, "wallets": old_wallets}
    new = Block(data=data)
    CyberCellCoin.add(new)

    for index in range(len(CyberCellCoin.nodes)):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        url = CyberCellCoin.nodes[index]
        url = url + "block"
        data = CyberCellCoin.latest_block.__dict__
        requests.post(url, json=data, headers=headers)

    for index in range(len(CyberCellCoin.nodes)):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        url = CyberCellCoin.nodes[index]
        url = url + "ping"
        data = request.url_root
        requests.post(url, json=data, headers=headers)

    print(not (request.url_root in CyberCellCoin.nodes))
    if (not (request.url_root in CyberCellCoin.nodes)):
        CyberCellCoin.nodes.append(request.url_root)
    return user_id

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
    sync_chain("http://0.0.0.0:8000/chain")
    sync_nodes("http://0.0.0.0:8000/peers")
    app.run(host='0.0.0.0', port=5000)