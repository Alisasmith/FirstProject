#!/usr/bin/env python
# encoding=utf-8
'''
@author: jszc
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 1558819350@qq.com
@software: garner
@file: FirstDemo.py
@time: 2017/5/18 9:19
@desc:
'''
# 键盘输入 raw_input()与input的区别
# 注意：raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收），
#                  将所有输入作为字符串看待，返回字符串类型；

#      input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，
#                否则它会引发一个 SyntaxError,在对待纯数字输入时具有自己的特性，
#                它返回所输入的数字的类型（ int, float ）。
#      input()本质上还是使用 raw_input() 来实现的，只是调用完 raw_input() 之后再调用 eval() 函数，
#              所以，你甚至可以将表达式作为 input() 的参数，并且它会计算表达式的值并返回它

# 长方形的面积
# print ("请输入长方形的长:")
# a = input()
# print ("请输入长方形的宽:")
# b = input()
#
# c = 0
# c = a * b
# print ("长方形的面积为："+str(c)+"m^2")

# ===================================list==============================
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]



