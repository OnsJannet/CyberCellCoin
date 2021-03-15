#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, send_file, jsonify, request
from models.wallet import Wallet
from models.chain import BlockChain
import requests
import json
app = Flask(__name__)
bch = BlockChain()

@app.route('/', strict_slashes=False)
def node():
    """ Prints a Message when / is called """
    return 'Node ready!'

@app.route('/wallet/<user_id>', methods=['POST'])
def create_wallet(user_id):
    wallet = Wallet(user_id)
    wallets = bch.latest_block.data["Wallets"].copy()
    wallets[wallet.user_id] = "00"
    late = bch.latest_block
    bch.construct_block(late.proof_nonce, late.prev_hash, [], wallets)
    print(bch.chain)
    return wallet.user_id

@app.route('/wallet/<user_id>', methods=['GET'])
def load_wallet(user_id):
    late = bch.latest_block
    if user_id in late.data['Wallets']:
        return late.data['Wallets'][user_id]
    return "No wallet"
    

@app.route('/blockchain', methods=['GET'], strict_slashes=True)
def get_blockchain():
    x = json.dumps(str(bch.chain))
    
    return jsonify(x)





if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
