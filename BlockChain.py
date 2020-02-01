#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:51:15 2019

@author: nitinkotcherlakota
"""

#Block chain

import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):
      
      self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
 
    def __str__(self):
        return 'Block information is shown below: \n Data: {} \n Timestamp: {} \n Hash: {} \n Previous Hash: {} \n '.format(self.data, self.timestamp, self.hash, self.previous_hash)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.tail = None
        self.block_count = 0
    def append(self, data):
        if self.block_count == 0:
            self.tail = Block(data, None)
        else:
            self.tail = Block(data, self.tail.hash)
        self.block_count += 1

    
blockchain = BlockChain()
blockchain.append('Information')
print(blockchain.tail)
blockchain.append('Some information')
print(blockchain.tail)
blockchain.append('Some more information')
print(blockchain.tail)
blockchain.append('')
print(blockchain.tail)

blockchain1 = BlockChain()
if (blockchain1.tail is None):
    print("There are no blocks in the blockchain")
else:
    print(blockchain1.tail)