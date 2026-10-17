#Triangle Type

#INPUT
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))

#PROCESS and OUTPUT
if a <= 0 or b <= 0 or c <= 0:
    print("Not a triangle")
elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Not a triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")

# BONUS: right-angled check
if (a + b > c) and (a + c > b) and (b + c > a):
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print("Also a right-angled triangle")