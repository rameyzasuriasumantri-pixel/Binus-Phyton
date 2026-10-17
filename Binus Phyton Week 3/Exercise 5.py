# Quadratic Equation Solver
import math

# INPUT
a = float(input("Enter value A: "))
b = float(input("Enter value B: "))
c = float(input("Enter value C: "))

# PROCESS & OUTPUT
if a == 0:
    print("It is not a quadratic equation")
else:
    discriminant = b ** 2 - 4 * a * c
    equation = f"{a}x² + {b}x + {c} = 0"

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("It has distinct roots")
        print(f"Equation: {equation}")
        print(f"Discriminant: {discriminant}")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminant < 0:
        print("It has imaginary roots")
        print(f"Equation: {equation}")
        print(f"Discriminant: {discriminant}")
        print(f"x1 = (-({b}) + sqrt({discriminant})) / (2 * {a})")
        print(f"x2 = (-({b}) - sqrt({discriminant})) / (2 * {a})")
    else:
        x = -b / (2 * a)
        print("It has a double root")
        print(f"Equation: {equation}")
        print(f"Discriminant: {discriminant}")
        print(f"x = {x}")