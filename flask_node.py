#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, send_file
from models.wallet import Wallet


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def node():
    """ Prints a Message when / is called """
    return 'Node ready!'

@app.route('/wallet/<user_id>', methods=['POST'])
def create_wallet(user_id):
    wallet = Wallet(user_id)
    wallet.create_keys()
    f = wallet.save_keys()
    return send_file(f.name , as_attachment=True)

@app.route('/wallet/<user_id>', methods=['GET'])
def load_wallet(user_id):
    wallet = Wallet(user_id)
    wallet.load_keys()
    res = {'User': wallet.user_id, 'Private': wallet.private_key, 'Public': wallet.public_key}
    return res

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
