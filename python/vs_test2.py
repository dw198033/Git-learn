

import string
import os
import numpy as np

'''
str = '1/2'
#str = input('please input a number: ')
s = str.split('/') 

print(int(s[0])+1)

'''
'''
srcPath = r'vs_test2.py'
path = os.path.abspath(srcPath)
print("abspath: ", path)

s = os.path.split(path)
print(s)
'''
'''
#idata
a1 = np.array([46,-49,60,-55,35,-36,-20,-33,-47,17,0,-47,63,-15,-26,-54])
a2 = np.array([-26,22,-50,-40,-17,2,-35,21,52,-38,15,0,18,5,32,-24])
a3 = np.array([46,15,60,9,35,28,44,31,17,17,0,17,63,49,38,10])
a4 = np.array([0,56,6,28,14,7,6,51,3,31,7,9,62,5,29,17])
a5 = np.array([29,16,45,21,23,24,20,8,29,54,36,51,13,34,21,3])

a6 = np.array([-11,-15,20,0,7,34,54,-19,21,15,43,37,-38,55,-63,12])
a7 = np.array([0,-10,4,29,-47,11,57,-51,19,22,46,34,-42,-56,53,-27])
a8 = np.array([24,29,48,1,-25,-35,-11,26,-42,-38,-63,-8,-2,29,-31,32])

# weight
b1 = np.array([12,47,41,-42,-4,22,59,-46,3,17,-16,-31,44,-29,-37,-19])
b2 = np.array([-30,6,5,-29,-58,-43,-8,-51,-45,1,4,49,-27,-8,58,48])
b3 = np.array([12,47,41,22,60,22,59,18,3,17,48,33,44,35,27,45])
b4 = np.array([1,50,21,50,1,1,5,34,20,59,48,13,51,14,54,6])

b6 = np.array([1,-21,-29,-56,-13,59,-60,15,36,22,23,16,-24,21,-50,58])

print(a8.shape)
print(b6.shape)

c = np.dot(a8,b6)
print(c)
'''

print('start python')
weight1 = np.array([1,2,3,4,5,6,7,8,9])
weight2 = np.array([1,57,7,29,15,8,7,52,4,32,8,10,63,6,30,18])

data1 = np.array([2,3,4,34,35,36,66,67,67])
data2 = np.array([54,53,47,48,39,3,16,54,6,5,9,19,34,33,48,56])

print(weight2.shape)
print(data2.shape)
c = np.dot(weight2,data2)
print(c)

print('run ok!')