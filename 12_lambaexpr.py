"""
Functional Programming Tools : Lambda Expression
"""


# Define function normally.
# write a function to calculate rectangle area by width,height
# rectangleArea :: (width:float, height: float) -> float

def rectangleArea(width: float, height: float) -> float:
    area: float = width * height
    return area


"""
lambda expression syntax
lambda <:arguments...> : <:expression>
"""

rect = lambda x, y: x * y
div2 = lambda x: x / 2  # y = f(x) =  x / 2
triangle = lambda x, y: div2(rect(x, y))

x = triangle(10, 20)
print("Triangle : ", x)

"""
higher order function

function :: (args) -> values
function :: (functions,args) -> values
function :: (functions,args) -> function
"""
from typing import Callable

rect = lambda a, b: a * b
triangle = lambda a, b: 1 / 2 * a * b
trapezoid = lambda a, b, c: 1 / 2 * (a + b) * c

rect_args = lambda a, b, *c : rect(a,b)
triangle_args = lambda a, b, *c : triangle(a,b)
trapezoid_args = lambda a, b, c, *d : trapezoid(a,b,c)

def calculate_area(calculator: Callable, *args):
    return calculator(*args)

print(calculate_area(rect_args, 4, 5, 6))
