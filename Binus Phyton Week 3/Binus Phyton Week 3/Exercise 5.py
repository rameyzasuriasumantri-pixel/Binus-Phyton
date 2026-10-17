# Quadratic Equation Solver

# INPUT
a = float(input("Enter value A: "))
b = float(input("Enter value B: "))
c = float(input("Enter value C: "))

# PROCESS & OUTPUT
if a == 0:
    print("It is not a quadratic equation")
else:
    discriminant = b ** 2 - 4 * a * c

    # Susun tampilan persamaan
    sign_b = "+" if b >= 0 else "-"
    sign_c = "+" if c >= 0 else "-"
    equation = f"{a}x² {sign_b} {abs(b)}x {sign_c} {abs(c)} = 0"

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print("It has distinct roots")
        print(f"Equation: {equation}")
        print(f"Discriminant: D = b² - 4ac = ({b})² - 4({a})({c}) = {discriminant}")
        print(f"x1 = (-b + √D) / 2a = (-({b}) + √{discriminant}) / (2 * {a}) = {x1}")
        print(f"x2 = (-b - √D) / 2a = (-({b}) - √{discriminant}) / (2 * {a}) = {x2}")
    elif discriminant < 0:
        print("It has imaginary roots")
        print(f"Equation: {equation}")
        print(f"Discriminant: D = b² - 4ac = ({b})² - 4({a})({c}) = {discriminant}")
        print(f"x1 = (-b + √D) / 2a = (-({b}) + √({discriminant})) / (2 * {a})")
        print(f"x2 = (-b - √D) / 2a = (-({b}) - √({discriminant})) / (2 * {a})")
    else:
        x = -b / (2 * a)
        print("It has a double root")
        print(f"Equation: {equation}")
        print(f"Discriminant: D = b² - 4ac = ({b})² - 4({a})({c}) = {discriminant}")
        print(f"x = -b / 2a = -({b}) / (2 * {a}) = {x}")