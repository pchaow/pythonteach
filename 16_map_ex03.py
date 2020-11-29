"""
ให้ l เป็นลิสต์ของ integer+ ใดๆ
อยากรู้ว่า  l เป็นลิสต์ของเลขจำนวนเฉพาะหรือไม่??
"""


# isPrime :: x:int -> bool
# x = 5 , d = [2,3,4]
def isPrime(x: int) -> bool:
    if x == 1:
        return False
    else:
        d = [i for i in range(2, int(x**0.5+1))]
        d2 = list(map(lambda a: x % a != 0, d))
        return True if all(d2) else False


# Program :: l : List[int] -> bool
# l = [1,2,3,4,5,6]
# l2 = [False,True,True,False,True,False]
# are_all_prime = False
l = [2, 3, 5, 7]
l2 = list(map(isPrime, l))
are_all_prime = all(l2)
print(are_all_prime)
