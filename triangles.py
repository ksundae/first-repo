import math
def find_hypotenuse(a,b):
    c = (a ** 2) + (b ** 2)
    hypotenuse = math.sqrt(c)
    return hypotenuse
print("Input two sides of the triangle, and we will find the hypotenuse!")
a = int(input("What is the first side of the triangle? "))
b = int(input("What is the second side of the triangle? "))
hypotenuse = find_hypotenuse(a,b)
print(f"The hypotenuse of your triangle is {hypotenuse}.")
