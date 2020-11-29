"""
reduce
"""

from functools import reduce

# l = [1, 2, 3, 4, 5]  # => 15
# x = reduce(lambda a, b: a * b, l,0)
# print(x)

# l = ['a', 'b', 'c', 'd', 'e']
# x = reduce(lambda x, y: x + y, l)
# print(x)

getmax = lambda x, y: x if x > y else y
l = [10, 2, 3, 4, 5]  # => 5
x = reduce(getmax, l)
# getmax(getmax(getmax(getmax(1,2),3),4),5)
print(x)
print(getmax(getmax(getmax(getmax(10,2),3),4),5))
