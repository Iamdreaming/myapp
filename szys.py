'''
@Coding: utf-8
@Description: 
@version: 
@Author: 陈锐填
@Date: 2020-03-29 14:59:02
@LastEditors: 陈锐填
@LastEditTime: 2020-03-29 14:59:02
@FilePath: \结对项目\szys.py
'''


import random
from random import randint


class SZYS():
    """生成四则运算"""

    def __init__(self, total, max):
        """
        total生成题目数量，max题目里数字最大数值
        """

        self.total = total
        self.max = max - 1
        self.operation = ['+', '-', '*', '/']

        #初始化文件
        with open('Exercises.txt','w') as f_n:
            f_n.write('')
        with open('Grade.txt','w') as f_o:
            f_o.write('')

    def create(self):
        # 生成式子并写进Exercise.txt
        formula = []
        operate_sum = [4, 6, 8]
        for i in range(1, random.choice(operate_sum)):
            if i % 2 == 0:
                formula.append(self.create_number())
            else :
                formula.append(random.choice(self.operation))

    def create_number(self):
        """
        随机返回数字 , 将分数存储为列表
        0 返回整数
        1 返回真分数如：五分之三表示为3/5
        2 返回假分数如：二又八分之三表示为2’3/8
        """
        i = randint(0, 1, 2)
        if i is 0:
            return randint(1, self.max)
        elif i is 1:
            fz = randint(1, self.max - 1)
            fm = randint(fz+1, self.max)
            return [fz, fm]
        else :
            add = randint(1, self.max)
            fz = randint(1, self.max - 1)
            fm = randint(fz+1, self.max)
            return [add, fz, fm]


    def select(self):
        return randint(0, 3)
