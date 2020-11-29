"""
Reduce Exercise
"""
from functools import  reduce
grades = ['a','b','c','a','a','b']
#มีเกรด 'a' อยู่กี่ตัว
x2 = reduce(lambda x,y:x + (1 if y == 'a' else 0),grades,0)
print('x',x2)
x = 0
for i in grades :
    x = x + (1 if i == 'a' else 0)

print('x',x)