"""
Assignment 2:
Create a function called "**isHappy(float)**.  This will return a boolean value that meets the following criteria:
* it is a number
* is an integer
* it is positive
"""

def isHappy(num):
#    if type(num) == str:
#      return False
    if type(num) != int:
        return False
    if num < 0:
        return False
    else:
        return True


print(
    isHappy("beans"),
    isHappy(2.0),
    isHappy(-2),
    isHappy(2),
)