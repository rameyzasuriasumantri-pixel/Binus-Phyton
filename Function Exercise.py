def identitas():
    print("---------------------")
    print("| Rameyza Alya S    |")
    print("|      Bintaro      |")
    print("---------------------")

def hitung(menu, value1=10, value2=5):
    if menu == "+":
        return value1 + value2
    elif menu == "-":
        return value1 - value2
    elif menu == "*":
        return value1 * value2
    elif menu == "/":
        return value1 / value2
    elif menu == "%":
        return value1 % value2

identitas()

menu = ""
while menu != "stop":
    menu = input("Enter Menu (+|-|/|*|%|stop): ")

    if menu == "stop":
        print("Program stopped. Thank you for using my program.")
    else:
        value1 = int(input("Enter Value 1: "))
        value2 = int(input("Enter Value 2: "))
        hasil = hitung(menu, value1, value2)

        if menu == "+":
            print("The result of addition", value1, "+", value2, "is", hasil)
        elif menu == "-":
            print("The result of subtraction", value1, "-", value2, "is", hasil)
        elif menu == "*":
            print("The result of multiplication", value1, "*", value2, "is", hasil)
        elif menu == "/":
            print("The result of division", value1, "/", value2, "is", hasil)
        elif menu == "%":
            print("The result of modulus", value1, "%", value2, "is", hasil)
        print()