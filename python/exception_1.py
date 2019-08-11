# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:35:54 2018

@author: 16012
"""

a = 1
b = 0

try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print (e)
    
finally:
    print ("done")
    
print('*' * 50)

try:
    name = input('Please input your name: ')
    print('Hello %s' %name)
    print(10/0)
    
except Exception as e:
    print('Got an error ', e)

finally:
    print('Game over')