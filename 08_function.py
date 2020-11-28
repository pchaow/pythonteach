"""
Function with Functional Programming (FP)
Concept

(There are 5 concepts but
Python can implement 3 concepts)

1. Pure function
2. Variables are Immutable
3. First Order or Higher Order Function


How to define a function

def <:name>(<:arguments>....) :
    <:statements>
    [return <:returnValues>
"""


# plus2 :: int -> int
def plus2(x: int) -> int:
    """
    ฟังก์ชั่น plus2 ทำการคำนวนค่า x+2
    :param x: เลขจำนวนเต็มใดๆ
    :return: เลขจำนวนเต็ม x+2
    """
    return x + 2


# factorial :: int -> int
def factorial(x: int) -> int:
    if x <= 0:
        return 1
    else:
        return x * factorial(x - 1)


# mysum(5) = 5 + 4 + 3 + 2 + 1
# mysum(5) = 5 + mysum(4)
# mysum(0) = 0
# mysum :: int -> int
def mysum(x: int) -> int:
    if x == 0:
        return 0
    else:
        return x + mysum(x - 1)


def mysum2(x: int) -> int:
    result = 0
    for i in range(x + 1):
        result += i
    return result


x = 100
y = mysum(x)
z = mysum2(x)
print(y, z)
