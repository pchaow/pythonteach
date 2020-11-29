"""
map Function
============

map (callable, iterable) -> mapObject

    l = [1,2,3,4,5]
    x = lambda x: x * 2
    สมมติว่า map (times2,l) จะได้ประมาณนี้
    l2 = [
        x(l[0]), x(l[1]), x(l[2]),...,x(l[n-1]),
    ]
"""

l = [1, 2, 3, 4, 5]
# l2 = [1,0,1,0,1]
l2 = list(map(lambda x: x % 2, l))
print("l2 :", l2)


