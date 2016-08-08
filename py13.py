#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: draon
@contact: maxiaolong@ict.ac.cn
@site: http://blog.csdn.net/zhzz2012
@software: PyCharm Community Edition
@file: py13.py
@time: 16-6-15 下午10:17
"""

# 下面这段程序计算一个数字转化成2进制后1到个数;

#思路是反复迭代，直到结果为0,迭代如果为偶数就减去1,并在计数上加1,如果是偶数就除以2;
def getNum(num):
    num_2 = 0
    if(num==0):
        return num_2
    if(num%2==0):
        return getNum(num/2)
    else:
        num_2=getNum(num-1)+1
        return num_2


if __name__ == '__main__':
    a=input("输入数字");
    print getNum(a)
    pass