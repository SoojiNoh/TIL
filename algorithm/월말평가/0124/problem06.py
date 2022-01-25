# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    
    _str = ""
    for w in word:
        _ascii = ord(w)+n
        if w.islower():
            if 122 < _ascii:
                _ascii -= 26
        else:
            if 96 < _ascii:
                _ascii -= 26
        _str += chr(_ascii)
    return _str
        
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('PYthon', 10))
    # Zidryx