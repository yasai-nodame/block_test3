import requests 
import json 
import datetime 

def main():
    time = datetime.datetime.now().isoformat()
    
    transaction = {
        "time":time,
        "sender":"A-san",
        "receiver":"B-san",
        "amount":111,
        "desctiption":"YYY Project Expenses",
        "signature":"signature_sample",
    }
    
    url = "https://block-test10.onrender.com/transaction_pool/"
    res = requests.post(url,json.dumps(transaction))
    
    """
    dumps関数とは、データをjson形式にエンコードすることのできる関数。エンコードとはデータを別の型に変換してくれること。
    json.dumps(transaction)は辞書型transactionをjson型に変換し、postメソッドで/transaction_poolにリクエスト送信している。
    """
    
    
    print(res.json())

if __name__ == "__main__":
    main()
