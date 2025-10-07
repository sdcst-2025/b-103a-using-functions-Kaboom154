"""
Assignment 1:
Create a function called **isNegative(float)** that takes a float parameter.  Return a boolean value to indicate whether the result is True or False
"""

def isNegative(floatNum):
    if type(floatNum) == str:
        return False
    return floatNum<0


print(
    isNegative(-2),
    isNegative(-2.0),
    isNegative(2),
    isNegative(2.0),
    isNegative("beans"),
)