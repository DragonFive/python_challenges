#!/usr/bin/env python
# coding=utf-8

#像这种计算列表中计算所有数字乘积末尾0的个数之类到问题，可以对每个元素进行2和5到质因数分解

#下面这个函数可以得到一个列表对2和5分解到结果和分解出2/5的个数和
def splitList(L):
	count_2=0; count_5=0
	newList=[]
	for item in L:
		while( item%2 == 0):
			count_2+=1;
			item = item/2;
		while( item%5 == 0):
			count_5 +=1;
			item = item/5;
		#把item加入一个列表里面;
		newList.append(item)
	
	return newList,count_2,count_5
# 其实最后发现返回最终到列表没什么用;

L = [2,8,3,50]
newList,count2,count5 = splitList(L)
#下面判断最后一个非零数字的奇偶性,如果质因数中5的个数比2多，说明2已经用完了，最终得到到就是奇数，否则是偶数;
if count2>count5:
	print count5
else:
	print count2

