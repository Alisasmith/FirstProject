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
import getpass
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
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print (lista[0])

# ===============================条件判断和循环==========================
#
age = 20
# if age >= 6:
#     print 'teenager'
# elif age >= 18:
#     print 'adult'
# else:
#     print 'kid'

#===============================循环====================================
# names = ['Lili', 'Alisa', 'Xiaoxiao']
# for name in names:
#     print name
#==================================计算0-100之和========================
# num = range(100)
# sum = 0
# for a in num:
#     sum=sum+a
# print sum

#=================================得到0-100之间的奇数 ====================
num = range(100)
n = len(num)
list_ou=[]
list_dan=[]
while n>0:
    if (num[n-1] % 2) == 0:
        list_ou.append(num[n-1])
    else:
        list_dan.append(num[n-1])
    n=n-1
print '偶数序列为：'+str(list_ou)
print '奇数序列为：'+str(list_dan)

# ======================Dictionary=====================
# 创建词典
phone_book = {'Tom': 123, 'Alisa': 456, 'LiLi': 759}

print ("Tom 的电话号码是："+str(phone_book['Tom']))
# 修改字典里面的值
phone_book['Tom'] = 963

print ("Tom 的电话号码是："+str(phone_book['Tom']))

# 想字典中添加元素
phone_book['zmf'] = 182

print ("zmf 的电话号码是："+str(phone_book['zmf']))

# 删除字典中的某个元素
del phone_book['zmf']
print ("字典内容为："+str(phone_book))

# 清除字典内容:将字典里的内容删掉，字典本身还存在
phone_book.clear()
print ("字典内容为："+str(phone_book))

# 删除字典：字典以及内容都被删除
del phone_book
# print ("字典内容为："+str(phone_book))

# 词典的特性 1）键值唯一，若同一个key值出现多次的话，会以最后一次的值为准
#           2）key值不可变，可用数字、字符串、元组充当键，不能通过list

# =====================function==def定义函数=======================
# 有参数没有返回值
def print_sum_two(a, b):
    c = a + b
    print ("a+b的值为："+str(c))
print_sum_two(3, 6)

# 有参数有返回值
def repeat_str(str, times):
    repeat_strs = str * times
    return repeat_strs

repeat_strings = repeat_str("Happy Birthday!", 4)
print (repeat_strings)





