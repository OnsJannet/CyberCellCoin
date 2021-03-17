#!/usr/bin/python3
from chain import BlockChain
from wallet import Wallet
from transactions import Transaction

bch = BlockChain()

w1 = Wallet("Abdou")
w2 = Wallet("Aymen")

tr = Transaction(w1 ,w2 ,"50000")
late = bch.latest_block
bch.construct_block(late.proof_nonce, late.prev_hash, tr.to_dict(), {w1.user_id: "00", w2.user_id: "00"})
tr1 = Transaction(w2 ,w1 ,"50000")
late = bch.latest_block
bch.construct_block(late.proof_nonce, late.prev_hash, tr1.to_dict(), {w1.user_id: "00", w2.user_id: "00"})

w3 = Wallet("Ons")
bch.construct_block(late.proof_nonce, late.prev_hash, [], {w1.user_id: "00", w2.user_id: "00", w3.user_id : "00"})


print(bch.chain)
