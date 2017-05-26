# coding=UTF-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 23:28
# @Author  : Aries
# @Site    : 
# @File    : Game.py
# @Software: PyCharm

from Tkinter import *
import tkMessageBox as mb
import tkSimpleDialog as dl
import web

# root = Tk() #设置主函数显示窗口
# w = Label(root, text='Guess Number Game') #设置弹窗标题
# w.pack()
#
# mb.showinfo("Welcome", 'Welcome Message')
#
# num = 59
# number_message = False
# while number_message == False:
#     input_num=dl.askinteger('Number','Enter an number')
#     if input_num>num:
#         mb.showinfo('输入大于目标数', '对不起，您输入的数字大于目标数字')
#     elif input_num<num:
#         mb.showinfo('输入小于目标数', '对不起，您输入的数字小于目标数字')
#     else:
#         number_message = True
# mb.showinfo('恭喜您', '恭喜您，猜对了')

# =============================创建网页===============================
urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greenting = "Hello World!"
        return greenting
if __name__ == "__main__":
    app.run()




