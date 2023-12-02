import requests
import json
import datetime
from ecdsa import SigningKey 
from ecdsa import SECP256k1 
import binascii 


def main(secret_key_str,sender_pub_key_str,receiver_pub_key_str,amount,description,url):
    time = datetime.datetime.now().isoformat()
    
    #署名データを生成するための辞書型
    transaction_unsigned = {
        "time":time,
        "sender":sender_pub_key_str,
        "receiver":receiver_pub_key_str,
        "amount":amount,
        "description":description
    }
    # binascii.unhexlify()で鍵情報を16進数文字列からバイト形式に変換している。
    # from_string()で鍵情報をバイト形式からKeyオブジェクトに変換している。
    secret_key = SigningKey.from_string(binascii.unhexlify(secret_key_str),curve=SECP256k1)
    
    signature_str = signature(transaction_unsigned,secret_key)

    #トランザクションプールに格納すうための辞書型
    transaction = {
        "time": time,
        "sender": sender_pub_key_str,
        "receiver": receiver_pub_key_str,
        "amount": amount,
        "description": description,
        "signature": signature_str #16進数文字列の署名データが入っている。
    }
    
    res = requests.post(url, json.dumps(transaction))
    print(res.json())
    
    
def signature(transaction_unsigned,secret_key):
    transaction_json = json.dumps(transaction_unsigned)
    transaciton_bytes = bytes(transaction_json,encoding="utf-8")
    signature = secret_key.sign(transaciton_bytes)#署名データを生成
    signature_str = signature.hex() #hex()で16進数文字列にし、ユーザー間のやりとりを行えるようにする
    return signature_str 

if __name__ == "__main__":
    url = "https://block-test10.onrender.com/transaction_pool/"
    secret_key_str = "538b0f6204354fc867167b7a5d33206b9a94b9ae533a5e4bc8e4c0c87836c023"
    sender_pub_key_str = "bfc8f858358167c61ad4458497a643cc0bc17585b1f01e93289ce015bd262a9cae7a84c7d6396726987fae6a046ea4bd44f7b7a51d8778a5c7eec117d753dfff"
    receiver_pub_key_str = "65828a3ea8f0570a0334a39b687bef63b170a65bfda8500b2c9c81318eab577763fe03da88dbad72c972e113bb9ebf41c12dfaf1b5a2b19af67ab1551709597b"
    amount = 222
    description = "Fee from B-san to A-san"
    
    main(secret_key_str,sender_pub_key_str,receiver_pub_key_str,amount,description,url)
