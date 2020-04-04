'''
@Coding: utf-8
@Description: 
@version: 
@Author: 陈锐填
@Date: 2020-03-29 14:59:02
@LastEditors: 陈锐填
@LastEditTime: 2020-04-04 21:00:01
@FilePath: \结对项目\szys.py
'''


import random
from random import randint
from fractions import Fraction
from stack import Stack


class SZYS():
    """生成四则运算"""

    def __init__(self, total, max):
        """
        total:生成题目数量
        max:题目里数字最大数值
        """

        self.total = total
        self.max = max - 1
        self.answer = []
        self.formula = []

        # 初始化文件
        with open('Exercises.txt', 'w') as f_n:
            f_n.write('')
        with open('Grande.txt', 'w') as f_o:
            f_o.write('')

    def store(self):
        # 调用create()，写入文件Exercise.txt,Grand.txt
        for i in range(1, self.total + 1):
            self.create_formula()
            with open('Exercises.txt', 'a') as f_n:
                f_n.write(str(i) + '. ')
                for item in self.formula[i-1]:
                    if type(item) is Fraction:
                        if item > 1:
                            num = item.numerator//item.denominator
                            item -= num
                            f_n.write("{}'{} ".format(num, item))
                        else:
                            f_n.write("{} ".format(item))
                    else:
                        f_n.write("{} ".format(item))
                f_n.write("\n")
            with open('Grande.txt', 'a') as f_o:
                f_o.write(str(i) + '. ' + str(self.answer[i-1]) + '\n')

    def create_formula(self):
        # 生成式子
        formula = []
        for i in range(1, self.select('operate_sum') + 1):
            if i % 2 == 1:
                formula.append(self.create_number())
            else:
                formula.append(self.select('operation'))

        # 计算答案
        answer = self.get_answer(formula)

        # 查重，当题目已有时重新调用create_formula()
        if self.is_equal(answer, formula) is True:
            self.create_formula()
        else:
            self.answer.append(answer)
            self.formula.append(formula)


    def get_answer(self, formula):
        """
        给出答案
        """
        # 创建一个栈，先处理所以的 * 和 /操作
        s = Stack()
        flag1 = 0
        for item in formula:
            if s.is_empty() is True:
                s.push(item)
            elif item == '*':
                flag1 = 1
            elif item == '/':
                flag1 = 2
            else:
                if flag1 == 0:
                    s.push(item)
                if flag1 == 1:
                    num = s.pop() * item
                    s.push(num)
                    flag1 = 0
                if flag1 == 2:
                    num = s.pop() / item
                    s.push(num)
                    flag1 = 0

        # 当栈里只剩一位时，即为答案
        if s.total() == 1:
            return s.pop()

        # 处理栈中的 加和减 操作，使用标志flag判断下个操作是否是减
        answer = 0
        flag = False
        for item in s.items:
            if item == '-':
                flag = True
            elif item != '+':
                if flag == True:
                    answer -= item
                else:
                    answer += item

        return answer

    def is_equal(self, answer, formula):
        # 查重 遍历储存的答案，若答案即题目的序号存储在列表equal
        equal = []
        for i in range(len(self.answer)):
            if answer == self.answer[i]:
                equal.append(i)

        # 判断相同答案对应的题目是否相同
        if len(equal) == 0:
            return False
        else:
            for i in equal:
                for item in formula:
                    if item not in self.formula[i]:
                        return False
            return True

    def create_number(self):
        """
        随机返回布尔值 , 将分数存储为列表
        True 返回整数
        False 返回分数如：五分之三表示为3/5
        """
        member = self.select('member')
        if member is True:
            return randint(1, self.max)
        else:
            fz = randint(1, self.max - 1)
            fm = randint(2, self.max)
            if fz % fm == 0:
                return self.create_number()
            else:
                return Fraction(fz, fm)

    def select(self, string):
        # 随机生成选择
        if string == 'operate_sum':
            # 返回式子的长度
            return random.choice([3, 5, 7])
        if string == 'member':
            return random.choice([True, False])
        if string == 'operation':
            return random.choice(['+', '-', '*', '/'])
