"""
Example 2 :
เขียนโปรแกรมเพื่อรับค่า r (รัศมีของวงกลม)
เพื่อแสดงพื้นที่ของวงกลมดังกล่าว
"""
import math

r: float = float(input("Enter Radius : "))
area: float = math.pi * (r ** 2)
# print("Area = ", area)
# แสดงค่า area ด้วยจุดทศนิยม 2 ตำแหน่ง
print(f"Area = {area:.2f}")
