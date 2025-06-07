import math

def Square(num):
    S = math.pow(num, 2)
    return S

def Log(num):
    S = math.log10(num)
    return S

def Quad(X, Y):
    S = math.sqrt(X**2 + Y**2)
    return S

print("The Square of a Number is:", Square(5))
print("The Log of a Number is:", Log(10))
print("The Quad of a Number is:", Quad(5, 2))