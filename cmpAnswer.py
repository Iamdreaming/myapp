'''
@Coding: utf-8
@Description: 校验答案
@version: 1.0
@Author: 何隽熙
@Date: 2020-04-13 15:30:22
@LastEditors: 陈锐填
@LastEditTime: 2020-04-14 16:49:06
@FilePath: \结对项目\cmpAnswer.py
'''


from fractions import Fraction
from szys import SZYS



def cmp(exerciseFile, answerFile, GrandeFile):
    correct = []
    wrong = []

    with open(exerciseFile, 'r', encoding='utf-8') as f_e:
        exercice = f_e.readlines()

    with open(answerFile, 'r', encoding='utf-8') as f_a:
        answerFile = f_a.readlines()
    j = 0
    for line in exercice:
        formula = line.split(' ')[1:-1]
        formula2 = []
        No = j + 1
        answer = answerFile[j].split('. ')[1]
        answer = answer.rsplit('\n')[0]
        if "'" in answer:
            answer1 = answer.split("'")
            answer2 = int(answer1[0]) + Fraction(answer1[1])
        else :
            answer2 =Fraction(answer)

        for i in range(0, len(formula)):
            if formula[i] not in ['+','÷','*','-','(',')']:
                try:
                    formula2.append(Fraction(formula[i]))
                except ValueError:
                    num = formula[i].split("'")
                    sum = int(num[0]) + Fraction(num[1])
                    formula2.append(sum)
            else:
                formula2.append(formula[i])
        j = j + 1
        answerTrue = SZYS.get_answer(SZYS, formula2)
        if answer2 == answerTrue:
            correct.append(No)
        else:
            wrong.append(No)
        

    saveToGrande(correct, wrong, GrandeFile)


def saveToGrande(correct, wrong, GrandeFile):
    with open(GrandeFile, 'w') as f_g:
        f_g.write(f'Correct:{len(correct)}{correct}\n'
                  f'Wrong:{len(wrong)}{wrong}')
