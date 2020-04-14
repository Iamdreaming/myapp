'''
@Coding: utf-8
@Description: gui
@version: 1.0
@Author: 陈锐填
@Date: 2020-04-12 15:31:16
@LastEditors: 陈锐填
@LastEditTime: 2020-04-14 16:20:22
@FilePath: \结对项目\gui.py
'''


import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from szys import SZYS
from cmpAnswer import cmp


class MyApp(tkinter.Frame):
    """
    gui界面
    """

    def __init__(self, master):
        super().__init__(master=master)
        self.frame = Frame(master)

        label_total = Label( text = '请输入题目数目')
        label_total.pack()
        self.entry_total = Entry()
        self.entry_total.pack()
        label_max = Label(text = '请输入数字最大值')
        label_max.pack()
        self.entry_max = Entry()
        self.entry_max.pack()
        self.buttom = Button(text='确定', command=self.input_sum)
        self.buttom.pack()
        self.pack()


        #校验答案
        self.buttom = Button(text='请选择题目文件', command=self.open_file1)
        self.buttom.pack()
        self.name1 = tkinter.Variable()
        self.entry = tkinter.Entry( textvariable=self.name1)
        self.entry.pack()

        self.buttom = Button(text='请选择答案文件', command=self.open_file2)
        self.buttom.pack()
        self.name2 = tkinter.Variable()
        self.entry = tkinter.Entry( textvariable=self.name2)
        self.entry.pack()

        self.buttom = Button(text='校验', command=self.examing)
        self.buttom.pack()
        self.pack()
        

    def input_sum(self):
        total = self.entry_total.get()
        max_num = self.entry_max.get()
        tkinter.messagebox.showinfo('提示','生成中，请耐心等待')
        s = SZYS(int(total), int(max_num))
        s.store()
        tkinter.messagebox.showinfo('提示','生成成功')

    def open_file1(self):
        # 获取文件名
        self.file_name1 = filedialog.askopenfilename()
        self.name1.set(self.file_name1.split(r'/')[-1])
    
    def open_file2(self):
        # 获取文件名
        self.file_name2 = filedialog.askopenfilename()
        self.name2.set(self.file_name2.split(r'/')[-1])
        
    def examing(self):
        cmp(self.file_name1,self.file_name2,'docs\\Grande.txt')
        tkinter.messagebox.showinfo('提示','校验成功，请查看文件Grande.txt')
    


def window():
    windows = Tk()
    windows.title("四则运算生成器")
    windows.geometry('400x400')
    welcome = Label(text='欢迎使用', fg='red', font=('Arial', 20))
    welcome.pack()
    myapp = MyApp(windows)
    windows.mainloop()


