"""
Loop

while <:condition> :
    statements

for <:variable> in <:iterable> :
    statements

"""

"""
เขียนโปรแกรมเพื่อพิมพ์เลข 1-10 ออกทางจอภาพ
1
2
...
10


# for
for i in range(1, 10 + 1):
    print(i)
    
# while
sp = 1
st = 10
while sp <= st:
    print(sp)
    sp += 1
"""

def pr(st: int, sp: int) -> None:
    if st == sp:
        print(st)
    else:
        pr(st + 1, sp)
        print(st)



pr(1,10)
