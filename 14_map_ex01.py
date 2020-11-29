"""
Exercise : Map01

l = [1,2,3,4,5,6,7,8,9,10]

แล้วต้องการ l2
l2 = ['a','aa','aaa','aaaa',.....,'aaaaaaaaaa']
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l2 = list(map(lambda x: x * 'a',l))
l2 = []
for i in l:
    f = lambda x: x * 'a'
    l2.append(f(i))
print(l2)