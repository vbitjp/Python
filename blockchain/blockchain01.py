# coding: utf-8
import json
import hashlib
import time

def calculate_hash(block):
    block_string = json.dumps(block).encode()
    return hashlib.sha256(block_string).hexdigest()


def proof_of_work(blockchain, previous_hash):
    nonce = 0
    while True:
        block = blockchain.create_block(nonce, previous_hash)
        guess_hash = calculate_hash(block)
        if guess_hash[:4] == "0000":
            break
            
        blockchain.chain.pop()
        nonce += 1
    return block


def mine(blockchain):
    previous_hash = calculate_hash(blockchain.chain[-1])
    proof_of_work(blockchain, previous_hash)
    blockchain.current_transactions = []
    blockchain.transaction_index = 0
    blockchain.create_transaction(sender='0', recipient="my_address", amount=1)
    block = blockchain.chain[-1]
    
    response = {
        'message': '新しいブロックを採掘しました',
        'index': block['index'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return response


def create_transactions(blockchain, values):
    required = ["sender", "recipient", "amount"]
    if not all([element in values for element in required]):
        return "valueの形式が正しくありません。"

    transaction_index, block_index = blockchain.create_transaction(values["sender"], values["recipient"], values["amount"])

    response = {"message": "トランザクションはブロック {block_index}の {transaction_index}番目 に追加されました"}
    return response


def chain(blockchain):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return response


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0
        self.create_transaction(sender='0', recipient="my_address", amount=1)
        proof_of_work(self, previous_hash = "00000")

    def create_block(self, nonce, previous_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transactions,
            'nonce' : nonce,
            'previous_hash' : previous_hash,
        }
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'transaction_index' : self.transaction_index,
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
            })
        self.transaction_index += 1
        return self.transaction_index - 1, len(self.chain)


blockchain = Blockchain()

values = {
    "sender" : "Akimoto",
    "recipient" : "Vbit",
    "amount" : 10
}

# 1.ブロックの追加
mine(blockchain)

# 2.マイニング
mine(blockchain)

# 3.トランザクション生成
create_transactions(blockchain, values)

# 4.トランザクション生成
create_transactions(blockchain, values)

# 5.マイニング開始
mine(blockchain)

# 6. 結果出力
#chain(blockchain)
print(chain(blockchain))
