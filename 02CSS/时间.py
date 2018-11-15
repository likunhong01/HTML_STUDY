#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/11/11 23:04'
__author__ = 'likunkun'


import time

h = time.strftime("%H",time.localtime())  #格式化字符串表示时间
if h<=12:
    print('上午好')
else:
    print('下午好')