#!user/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci series"""

import decimal


def lexicographics(to_analyze):
    maxline = 0
    minline = 0
    counter = 0
    to_analyze = to_analyze.split('\n')
    for line in to_analyze:
       words = line.split()
       print len(words)
       # to_analyze[counter] = words
       # maxline = len(max(to_analyze))
       minline += len(min(words))
       # counter += 1

     
        

    return to_analyze, (maxline, minline), words

STRING = ('This the first line of a string in Python\n'
          'that has multiple lines, in fact there are three lines total\n'
          'and this is the last one.')

print lexicographics(STRING)



    
