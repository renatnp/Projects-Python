import math

a = float(input("Enter the value of term 'a': "))
b = float(input("Enter the value of term 'b': "))
c = float(input("Enter the value of term 'c': "))

if a == 0:
    print("Cannot be calculated")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Cannot be calculated")
    else:
        root1 = (-b + (math.sqrt(delta))) / (2*a)
        root2 = (-b - (math.sqrt(delta))) / (2*a)

        print(f"X1 = {root1:.5f}")
        print(f"X2 = {root2:.5f}")