"""
Conditional

if (condition) :
    statements
elif (condition) :
    statements
else :
    statements
"""


def main():
    """โปรแกรมคำนวณพื้นที่รูปเลขาคณิตต่างๆ
    กด 1 พื้นที่สี่เหลี่ยมผืนผ้า
    กด 2 พื้นที่สามเหลี่ยม

    การทำงาน
    1. แสดงเมนู
    2. รับค่าเมนูที่ผู้ใช้เลือก
    3. ตัดสินใจว่าจะคำนวณอะไร?????
        3.1 ผู้ใช้กด 1 คำนวณพื้นที่ 4 เหลี่ยมผืนผ้า
        3.2 ผู้ใช้กด 2 คำนวณพื้นที่ 3 เหลี่ยม
    4. จบโปรแกรม

    แผนการทำงาน
    1. def showMenu() -> None
    2. def calRectangleArea() -> None
    3. def calTriangleArea() -> None

    """

    # 1. แสดงเมนู
    showMenu()
    # 2. รับค่าเมนูที่ผู้ใช้เลือก
    choice: int = int(input("Select Menu : "))
    #3. ตัดสินใจว่าจะคำนวณอะไร?????
    if choice == 1 :
        # 3.1 ผู้ใช้กด 1 คำนวณพื้นที่ 4 เหลี่ยมผืนผ้า
        calRectangleArea()
    else :
        # 3.2 ผู้ใช้กด 2 คำนวณพื้นที่ 3 เหลี่ยม
        calTriangleArea()
    #จบโปรแกรม


main()
