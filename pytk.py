#_*_coding:utf-8_*_

# 使用时直接将该文件放在同目录下，或者Python的sys.path中即可
# 引用时使用from pytk import pytk即可

def outTest():
    print('outTest')

class pytk:
    """Toolkit for Python written by TopXeQ"""

    pytkVersion = '0.99a'

    @classmethod
    def test(cls):
        print('test')

if __name__ == '__main__': 
    pytk.test()

