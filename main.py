from fastapi import FastAPI 
import blockchain
from pydantic import BaseModel

class Transaction(BaseModel):
    time:str 
    sender:str 
    receiver:str 
    amount:int 
    desctiption:str 
    signature:str 
    

blockchain = blockchain.BlockChain()

app = FastAPI() 


@app.get("/transaction_pool")
def get_transaction():
    #トランザクションプールをブラウザに表示させる処理
    return blockchain.transaction_pool

@app.get("/chain")
def get_chain():
    #チェーンをブラウザに表示させる処理
    return blockchain.chain

@app.post("/transaction_pool")
def post_transaction_pool(transaction:Transaction):
    #トランザクションをトランザクションプールに追加する処理
    blockchain.add_transaction_pool(transaction)
    return {"message":"Transaction is posted."}

@app.get("/create_block/{creator}")
def create_block(creator:str):
    #ブロック生成処理
    blockchain.create_new_block(creator)
    return {"message":"New Block is Created"}