'''
@Coding: utf-8
@Description:
@version:
@Author: 陈锐填
@Date: 2020-03-29 14:59:02
@LastEditors: 陈锐填
@LastEditTime: 2020-04-14 16:20:31
@FilePath: \结对项目\szys.py
'''

import random
from fractions import Fraction
from random import randint


class SZYS():
    """生成四则运算"""

    def __init__(self, total, max):
        """
        total:生成题目数量
        max:题目里数字最大数值
        """

        self.total = total
        self.max = max - 1
        self.answer = {}
        self.formula = {}
        self.formula2 = []
        # 初始化文件
        with open('docs\\Exercises.txt', 'w', encoding='utf-8') as f_n:
            f_n.write('')
        with open('docs\\Answers.txt', 'w') as f_o:
            f_o.write('')

    def store(self):
        # 调用create()，写入文件Exercise.txt,Answers.txt

        for i in range(1, self.total + 1):
            self.create_formula(i)
        with open('docs\\Answers.txt', 'a', encoding='utf-8') as f_o:
            for i in range(1, self.total +1 ):
                f_o.write(str(i) + '. ')
                if self.answer[i] > 1 and self.answer[i].denominator > 1:
                    num = self.answer[i].numerator // self.answer[i].denominator
                    self.answer[i] -= num
                    f_o.write("{}'{} ".format(num, self.answer[i]))
                else :
                    f_o.write("{} ".format(self.answer[i]))
                f_o.write('\n')
        i = 0
        with open('docs\\Exercises.txt', 'a', encoding='utf-8') as f_n:
            for formula in self.formula.values():
                i = i + 1
                f_n.write(str(i) + '. ')
                for item in formula:
                    if type(item) == Fraction:
                        if item > 1 and item.denominator > 1:
                            num = item.numerator // item.denominator
                            item -= num
                            f_n.write("{}'{} ".format(num, item))
                        else :
                            f_n.write("{} ".format(item))
                    elif item == '/':
                        f_n.write('÷ ')
                    else :
                        f_n.write("{} ".format(item))
                f_n.write("=\n")

    def create_formula(self, i):
        # 生成式子
        formula = []
        local = 0
        flag = False
        operate_sum = self.select('operate_sum') + 1
        for j in range(1, operate_sum):
            if j % 2 == 1 : 
                if self.select('kuohao') and flag is False:
                    if operate_sum  - j >= 3:
                        formula.append('(')
                        local = j
                        flag = True
                formula.append(self.create_number() )
                if flag is True and j!= local:
                    formula.append(')')
                    flag = False
            else :
                formula.append(self.select('operation'))
        formula2 = set(formula)

        # 查重，当题目已有时重新调用create_formula()
        if self.is_equal(formula2) is True:
            self.create_formula(i)
        else:
            answer = self.get_answer(formula)
            if answer < 0 or answer is False:
                self.create_formula(i)
            else:
                self.answer[i] = answer
                self.formula2.append(formula2)
                self.formula[i] = formula


    def get_answer(self, formula):
        """
        将式子转化为字符串，利用eval及python内置计算
        由于直接计算结果为小数，姑在每个数字前乘与Fraction(1,1)
        给出答案
        """
        try:
            answer = ''
            for item in formula:            
                if type(item) is Fraction:
                    answer += '(Fraction(1,1) *' + str(item) + ')'
                # 将除号标准化
                elif item == '÷':
                    answer += '/'
                else :
                    answer += item
            return  eval(answer)
        except ZeroDivisionError:
            return False

       
    def is_equal(self, formula2):
        # 查重
        if formula2 in self.formula2:
            return True
        return False

    def create_number(self):
        """
        随机返回布尔值 , 将分数存储为列表
        True 返回整数
        False 返回分数如：五分之三表示为3/5
        """
        member = self.select('member')
        if member is True:
            fz = randint(1, self.max - 1)
            fm = 1
            return Fraction(fz, fm)
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
        if string == 'kuohao':
            return random.choice([True,False])
