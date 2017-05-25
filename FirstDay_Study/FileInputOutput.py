#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 0:45
# @Author  : Aries
# @Site    : 
# @File    : FileInputOutput.py
# @Software: PyCharm

# ====================读写文件 File IO=====================
# some_sentences = '''
# Anywhere you are I am near
# Anywhere you go I'll be there
# Anytime you whisper my name
# You'll see
# How every single promise I'll keep
# 'Cause what kind of guy would I be
# If I was to leave
# When you need me most
# What are words
# If you really don't mean them
# When you say them
# What are words
# If they're only for good times
# Then they're done
# '''
# new_file = open('E:\sentences.txt','w')
# new_file.write(some_sentences)
# new_file.close()

# ===================读文件===============
# read_file = open('E:\sentences.txt','r')
# while True:
#     line = read_file.readline()
#     if len(line) == 0:
#         break
#     print (line)
# read_file.close()

# ===================序列化=====================
# Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，
# pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle
# 创建对象序列化并存入到文件中
# pic_dict = {'name':'Tom', 'age':8, 'sex':'man', 'address':'Beijing'}
# f = open("dump.txt", "wb")
# pickle.dump(pic_dict, f)
# f.close()



# ==================反序列化======================
# pickle.load出现EOFError  EOFError一般是因为读到了空文件的时候出发，因此当load的时候catch一下这个异常
f = open('dump.txt', 'rb')
try:
    print pickle.load(f)
except:
    print '没有内容'
f.close()



