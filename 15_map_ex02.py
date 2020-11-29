"""
all and any functions

all([l1,l2,....ln])
    -> True เมื่อ l  ทุกตัวเป็น True
    -> False เมื่อ มี False อย่างน้อย 1

any([l1,l2,....ln])
-> True เมื่อ True อย่างน้อย 1
-> False เมื่อ l  ทุกตัวเป็น False
"""

# def isEven(x):
#     # if x % 2 == 1:
#     #     return False
#     # else:
#     #     return True
#     return True if x % 2 == 0 else False
#
#

is_even = lambda x: True if x % 2 == 0 else False
is_odd = lambda x: not is_even(x)
l = [2, 4, 6]
# อยากรู้ว่า l เป็นเลขคู่ทุกตัวใหม?
# l2 = [False,True,False,True,False,True]
#l2 = list(map(is_even, l))
l2 = list(map(is_odd,l))
# all(l2) -> False
#all_even = all(l2)
any_odd = any(l2)
print('Were l all even? : ', not any_odd)
