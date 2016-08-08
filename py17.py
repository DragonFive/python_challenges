#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: draon
@contact: maxiaolong@ict.ac.cn
@site: http://blog.csdn.net/zhzz2012
@software: PyCharm Community Edition
@file: py17.py
@time: 16-7-3 下午5:27
"""

# 求解100以内到所有素数
def isSushu(a):
    if a<4:
        return 0
    for i in range(2,a-1):
        if a%i==0:
            return 1
    return 0
print ' '.join([str(i) for i in range(2, 101) if not isSushu(i)])

from math import sqrt
print ' '.join([str(i) for i in range(2, 101) if 0 not in [ i%j for j in range(2,int(sqrt(i))+1)  ]   ])
if __name__ == '__main__':
    print ' '.join([str(i) for i in range(2, 101) if not isSushu(i)])
    pass