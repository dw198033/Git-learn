
import numpy as np
import cv2
'''
print("hello, vs code")

a = 3
b = 5
c = a + b

print(c)


d1 = np.array([128,-214,-24,-164,-38,-113,-78,-23,103,92,-214,138,-90,96,143,80])
d2 = np.array([-237,44,-253,-128,-118,63,-78,-47,-180,148,-190,210,95,-195,52,-214])
d3 = np.array([128,42,232,92,72,77,95,37,216,184,198,182,144,247,94,6])
f = np.sum(d3)

print(f)
'''
import re
key = r"mat cat hat pat"
p1 = r"[^c|p]at"
pattern1 = re.compile(p1)
print (pattern1.findall(key))

line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
