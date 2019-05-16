#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/10 16:30 
# @Author : wanxin
# @File : calc.py 
# @Software: PyCharm




def getSubInteger(n):
  min =1
  max =1
  sum =0
  temp = n
  count =0;
  while 1:
    str = "1 + "
    if count ==0:
      str += "%d" % (temp - 1)
      temp -= 1
    else:
      for x in range(count):
       str = str + "1 + "
      str += "%d" %(temp-1)
      temp -=1
    count +=1
    print(str)
    if temp ==1:
      break



    # if sum == n:
    #   for k in range (min,max-1):
    #     if k<max-1:
    #       print("%d + %d" %(n,k))
    #     else:
    #       print("%d + %d" %(n,k))
    #   max = min
    #   sum =0
    # elif sum > n:
    #     sum =0
    #     min+=1
    #     max = min
    # else:
    #     sum =sum +max
    #     max+=1
    #

getSubInteger(7)