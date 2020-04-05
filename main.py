'''
@Coding: utf-8
@Description: 
@version: 
@Author: 陈锐填
@Date: 2020-03-27 19:07:54
@LastEditors: 陈锐填
@LastEditTime: 2020-04-05 15:25:37
@FilePath: \结对项目\main.py
'''
"""
@Coding: utf-8
@Description:
@version:
@Author: 陈锐填
@Date: 2020-03-27 19:07:54
@LastEditors: 陈锐填
@LastEditTime: 2020-03-29 11:48:21
@FilePath: \结对项目\main.py
"""
from time import time
from szys import SZYS
def main():
    a = SZYS(10000,10)
    a.store()

if __name__ == '__main__':
    t1 = time()
    main()
    t2 = time()
    print(t2-t1)