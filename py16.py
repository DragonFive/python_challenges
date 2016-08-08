#!/usr/bin/env python
# encoding: utf-8


"""
@version: python2.7
@author: draon
@contact: maxiaolong@ict.ac.cn
@site: http://blog.csdn.net/zhzz2012
@software: PyCharm Community Edition
@file: py16.py
@time: 16-6-16 下午8:04
"""

hans='零壹贰叁肆伍陆柒捌玖'
weis ='圆拾佰仟万拾佰仟'



if __name__ == '__main__':
    num = 1234567
    strNum = str(num)
    #i表示第几位,位置上的数表示第几个
    str = ''
    for i in range(len(strNum)-1,0,-1):
        str+=hans[int(strNum[len(strNum)-1])]
        str += weis[i]

    print str.decode("utf-8")

    pass