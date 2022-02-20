"""単純にハッシュ化したい場合のサンプル
hashlibは、Python標準ライブラリ
"""
import hashlib



def do_hashing(s:str) -> str:
    """文字列をハッシュ化して返す

    Args:
        s (str): _description_

    Returns:
        str: _description_
    """
    s_bin = s.encode()
    
    hashed_bin = hashlib.md5(s_bin)
    #hashed_bin = hashlib.sha256(s_bin)
    #hashed_bin = hashlib.sha3_256(s_bin)
    
    print(f'method: {hashed_bin.name}')
    
    hashed_str = hashed_bin.hexdigest()
    return hashed_str


import time
def measure_time():
    """ハッシュの時間を計測する
    """
    s = 'testの文字列123!'
    kurikaeshi = 500000
    
    # md5
    start_time = time.process_time()
    for _ in range(kurikaeshi):
        _ = (hashlib.md5(s.encode())).hexdigest()
    end_time = time.process_time()
    elapsed_time_md5 = end_time - start_time
    print(f'md5     : {elapsed_time_md5}(s)  100%')
    
    # sha256
    start_time = time.process_time()
    for _ in range(kurikaeshi):
        _ = (hashlib.sha256(s.encode())).hexdigest()
    end_time = time.process_time()
    elapsed_time_sha256 = end_time - start_time
    print('sha256  : %f(s)  %d%%' % (elapsed_time_sha256, int(elapsed_time_sha256*100/elapsed_time_md5)))
    
    # sha3_256
    start_time = time.process_time()
    for _ in range(kurikaeshi):
        _ = (hashlib.sha3_256(s.encode())).hexdigest()
    end_time = time.process_time()
    elapsed_time_sha3_256 = end_time - start_time
    print('sha3_256: %f(s)  %d%%' % (elapsed_time_sha3_256, int(elapsed_time_sha3_256*100/elapsed_time_md5 )))
    
    # hexdigest()をつけると
    # md5:100, sha256:115, sha3_256:135 くらいか
    
    # hexdigest()をつけないと100, 105, 105くらい。文字列化のコストはかなり大きい。
    # md5は32文字、sha256,sha3_256は64文字だけど、後者に差が出るのが謎。
    

if __name__=='__main__':
    str_hash = do_hashing('aiuえおかきくkeko')
    print(str_hash)
    #measure_time()
    