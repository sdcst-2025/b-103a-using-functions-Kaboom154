"""
Assignment 4:
Create a function called **isPythagoreanTriple(a,b,c)**.  This will return a True value if the 3 numbers form a pytyagorean triple.  Note that you will ahve to decide which number would be the hypotenuse
"""

def isPythagoreanTriple(a,b,c):
    if (c**2) == ((a**2)+(b**2)):
        return True
    else:
        return False


print(
    isPythagoreanTriple(3,4,5),
    isPythagoreanTriple(5,12,13),
    isPythagoreanTriple(1,1j,0),
    isPythagoreanTriple(1,2,3),
)