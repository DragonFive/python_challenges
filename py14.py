#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: draon
@contact: maxiaolong@ict.ac.cn
@site: http://blog.csdn.net/zhzz2012
@software: PyCharm Community Edition
@file: py14.py
@time: 16-7-3 下午6:03
"""

# 计算两个整数公约数的个数
# 思路就是计算公约数到约数个数
a=8
b=10
print len([i for i in xrange(1,b+1) if b%i==0 and a%i==0])

if __name__ == '__main__':
    pass