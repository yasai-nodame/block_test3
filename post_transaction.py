import requests 
import json 
import datetime 

def main():
    time = datetime.datetime.now().isoformat()
    
    transaction = {
        "time":time,
        "sender":"E-san",
        "receiver":"F-san",
        "amount":999,
        "desctiption":"Study Books Fee",
        "signature":"signature_sample",
    }
    
    url = "https://block-test8.onrender.com/transaction_pool/"
    res = requests.post(url,json.dumps(transaction))
    
    """
    dumps関数とは、データをjson形式にエンコードすることのできる関数。エンコードとはデータを別の型に変換してくれること。
    json.dumps(transaction)は辞書型transactionがtransaction型になるということ。
    
    辞書型transactionのデータをtransaction型に変更しpostメソッドで/transaction_poolにリクエスト送信している。
    """
    
    
    print(res.json())

if __name__ == "__main__":
    main()