def showMenu():
    print("กด 1 เพื่อคำนวณพื้นที่สี่เหลี่ยม")
    print("กด 2 เพื่อคำนวณพื้นที่สามเหลี่ยม")
    pass


def calRectangleArea():
    a:float = float(input('Enter high'))
    b:float = float(input('Enter width'))
    c:float = a * b
    print(c)
    pass


def calTriangleArea():
    b : float = float(input("Enter your base = "))
    h : float = float(input("Enter your High = "))
    area = 1/2 * b * h
    print(area)
    pass

def main():
    showMenu()
    choice: int = int(input("Select Menu : "))
    if choice == 1:
        calRectangleArea()
    else:
        calTriangleArea()

main()
