# Triangle Type (While Loop)

ulang = "Y"

while(ulang == "Y"):
    # INPUT
    a = float(input("Enter Side A: "))
    b = float(input("Enter Side B: "))
    c = float(input("Enter Side C: "))
    print()

    # PROCESS and OUTPUT
    if a <= 0 or b <= 0 or c <= 0:
        print("Not a triangle")
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Not a triangle")
    elif a == b == c:
        print("It is an Equilateral Triangle")
    elif a == b or a == c or b == c:
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")

    # BONUS: right-angled check
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            print("Also a right-angled triangle")

    print()
    ulang = input("Do you want to repeat? ")
    print()

print("Program Stops")
print("Thank you for using my program ^^")