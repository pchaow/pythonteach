"""
Exercise 1 : Basic Filtering
ให้ scores เป็นลิสต์ของคะแนนของนักเรียน
อยากรู้ว่ามีนักเรียนกี่คนที่ได้เกรด A
grade :
    7-10 A
    5-7  B
    0-5  C
"""
def grader(score):
    if 7 <= score <= 10:
        return 'A'
    elif 5 <= score < 7:
        return 'B'
    else:
        return 'C'

scores = [8, 7, 6, 5, 4, 6, 1, 2, 5, 6, 9, 8, 7, 4, 5, 10, 7, 5]
#write your code after here.