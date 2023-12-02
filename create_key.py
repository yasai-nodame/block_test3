from ecdsa import SigningKey 
from ecdsa import SECP256k1 

def main():
    #SECP256k1曲線を利用した秘密鍵を生成
    secret_key = SigningKey.generate(curve=SECP256k1)
    
    #秘密鍵から公開鍵を生成
    public_key = secret_key.verifying_key 
    
    #秘密鍵をKeyオブジェクトから16進数文字列に変換
    secret_key_str = secret_key.to_string().hex() #　to_stringでkeyオブジェクトからバイト形式にしている。hex()は、bytesオブジェクトから16進数の文字列を生成する。
    
    #公開鍵をKeyオブジェクトから16進数文字列に変換
    public_key_str = public_key.to_string().hex()
    
    key = {"secret_key_str":secret_key_str,"public_key_str":public_key_str}
    print(key)
    

if __name__ == "__main__":
    main()