'''
@coding: utf-8
@Description: 栈
@version: 1.0
@Author: 陈锐填
@Date: 2020-03-29 10:47:46
@LastEditors: 陈锐填
@LastEditTime: 2020-04-04 19:38:34
@FilePath: \结对项目\stack.py
'''


class Stack():
    """栈"""

    def __init__(self):
        # 创建一个空的列表
        self.items = []

    def is_empty(self):
        # 判空
        return self.items == []

    def push(self, item):
        # 入栈
        self.items.append(item)

    def pop(self):
        # 出栈
        return self.items.pop()

    def items(self):
        return self.items

    def total(self):
        return len(self.items)
