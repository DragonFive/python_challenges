#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: draon
@contact: maxiaolong@ict.ac.cn
@site: http://blog.csdn.net/zhzz2012
@software: PyCharm Community Edition
@file: py18.py
@time: 16-6-17 下午5:33
"""

# 下面的函数用来计算两个函数到最大公约数;
def gcd(a,b):
    while b%a!=0:
        b,a=a,b%a
    return a
    pass

# 下面计算公约数位m，公倍数位n到两个数
def inverseYueBei(m,n):
    #  从n到m判断每一个数符不符合约数和倍数到条件
    container = []
    for i in range(m,n+1,m):
        content = []
        if m*n%i==0:    #说明能够整除；
            j = m*n/i
            if i>j:
                break

            elif j%m==0: #这一组数据符合要求;
                temp = gcd(i,j)
                if temp == m:
                    content.append(i)
                    content.append(j)
                    container.append(content)
                pass


    return container
    pass


if __name__ == '__main__':
    container = inverseYueBei(2,40)
    for content in container:
        print ' '.join(map(str,content))
    pass
