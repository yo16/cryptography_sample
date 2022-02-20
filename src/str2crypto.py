"""文字列（パスワード）から鍵（バイナリ）を生成
"""
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def str2crypto(pwd:str, salt:bytes=None) -> [bytes, bytes]:
    """文字列から鍵を生成

    Args:
        pwd (str): 文字列。パスワード文字列を想定。
        salt (bytes, optional): 鍵生成のためのソルト.スペル注意. Defaults to None.

    Returns:
        [bytes, bytes]: 鍵, salt
    
    Note:
        ハッシュ化は下記で実装しており、この中から選べる.
        https://github.com/pyca/cryptography/blob/main/src/cryptography/hazmat/primitives/hashes.py
    """
    # saltの指定がない場合は作成
    if not salt:
        salt = create_salt()
    #print(salt)
    
    # パスワードをエンコード（バイナリ化）
    pwd_bin = pwd.encode()
    #print(pwd_bin)
    
    # KDF(Key Derivation Function, 鍵を作る関数)を作成
    kdf = PBKDF2HMAC(
        #algorithm=hashes.MD5(),
        #algorithm=hashes.SHA256(),
        algorithm=hashes.SHA3_256(),
        length=32,
        salt=salt,
        iterations=100003,  # 10万回以上が奨励されており、回数は秘密情報
        backend=default_backend()
    )
    
    # 鍵を生成
    key = base64.urlsafe_b64encode(kdf.derive(pwd_bin))
    
    return key, salt


def create_salt() -> bytes:
    """文字列から鍵を生成する際の乱数バイナリ(salt)を生成
    
    一度作ったら、文字列から鍵を使う際にはそのsaltを使う。

    Returns:
        bytes: salt
    """
    return os.urandom(16)


if __name__=='__main__':
    print('Enter string:')
    s = input()
    b, salt = str2crypto(s)
    print(b, salt)
    
    print('Varidation!')
    b2, salt2 = str2crypto(s, salt)
    print(b2, salt2)
    assert b==b2, "同じものが生成されるはず"
    assert salt==salt2, "変えてないから同じはず(salt)"
    
    # ついでに、"文字列をハッシュ化したい"という文脈でよく使われるので
    # base64を文字列化
    b_str = b2.decode()
    print(b_str)
    # base64の作り方的に、ただb'～'のbが取れただけのような形
    
