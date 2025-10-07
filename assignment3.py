'''
Assignment 3:
Create a function called **isPerfectSquare(float)**.  This will return a True value if the number is a perfect square
'''
import math

def isPerfectSquare(num):
    if type(num) == str:
        return False
    num = int(num)
    if num<0:
        return False
    if (math.isqrt(num))**2 != num:
        return False
    else:
        return True


print(
    isPerfectSquare(4),
    isPerfectSquare(4.0),
    isPerfectSquare(2),
    isPerfectSquare(-4),
    isPerfectSquare("beans"),
)