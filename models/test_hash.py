#!/usr/bin/python3
import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())
print(m.digest_size)
32
print(m.block_size)
