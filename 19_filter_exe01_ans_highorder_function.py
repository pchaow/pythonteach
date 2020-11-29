"""
Exercise 1 : Basic Filtering
ให้ scores เป็นลิสต์ของคะแนนของนักเรียน
อยากรู้ว่ามีนักเรียนกี่คนที่ได้เกรด A
grade :
    7-10 A
    5-7  B
    0-5  C
"""
from typing import Callable


def getFuncCountGrade(grader: Callable, grade: str):
    return lambda scores: len(
        list(
            filter(lambda x: grader(x) == grade, scores)
        )
    )

def graderOOP(score):
    if 7 <= score <= 10:
        return 'A'
    elif 5 <= score < 7:
        return 'B'
    else:
        return 'C'

def graderPython2(score) :
    if 6 <= score <= 10:
        return 'A'
    elif 4 <= score < 6:
        return 'B'
    else:
        return 'F'

graderFunction = {
    'oop' : graderOOP,
    'python2' : graderPython2,
}

print("Grader Program ")
g = input("Enter grader [oop/python2] : ")
countA = getFuncCountGrade(graderFunction[g],'A')


scores = [8, 7, 6, 5, 4, 6, 1, 2, 5, 6, 9, 8, 7, 4, 5, 10, 7, 5]
# write your code after here.

print(countA(scores))


