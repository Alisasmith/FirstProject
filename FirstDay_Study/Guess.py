# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 22:12
# @Author  : Aries
# @Site    : 
# @File    : Guess.py
# @Software: PyCharm
# 导入GUI界面

from Tkinter import*
import tkSimpleDialog as dl
import tkMessageBox as mb

root=Tk() #创建主函数显示框  Tk() 是Tinker自带的构造函数
w = Label(root,text = "Label Title") #root  主函数框，text  显示的主体框的标题
w.pack()

mb.showinfo('Welcome', 'Welcome Message')
guess = dl.askinteger('Number', 'Enter an number') #用户输入框

output = 'This is output message'
mb.showinfo('Output:', output)