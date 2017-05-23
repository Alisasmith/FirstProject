# coding=UTF-8
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
read_file = open('E:\sentences.txt','r')
while True:
    line = read_file.readline()
    if len(line) == 0:
        break
    print (line)
read_file.close()