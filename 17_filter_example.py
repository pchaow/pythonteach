"""
Filter
=======

filter( (any) -> bool , iterable) -> iterable

** iterable คือค่าที่สามารถเอาไปวนลูปได้ เช่น list string tuple dict etc.

"""

l = [
    {'name': 'John', 'age': 18},
    {'name': 'Alice', 'age': 6},
    {'name': 'Roger', 'age': 5},
    {'name': 'Edison', 'age': 19},
]

# แสดง ชื่อของคนที่อายุน้อยกว่า 15 ปี
''' filter
l2 = [
    {'name': 'Alice', 'age': 6},
    {'name': 'Roger', 'age': 5},
]
'''
l2 = list(filter(lambda x: x['age'] <= 15, l))

''' map
l3 = [ 'Alice','Roger']
'''
l3 = list(map(lambda x: x['name'], l2))

for i in l3:
    print(i)
'''
for i in l :
    if i['age'] <= 15 :
        print(i['name'])
'''
