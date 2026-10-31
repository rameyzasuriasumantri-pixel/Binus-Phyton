ulang = "Y"

while(ulang == "Y"):
    angka = int(input("Enter any number: "))

    if angka % 2 == 0:
        print("The number " + str(angka) + " is even")
    else:
        print("The number " + str(angka) + " is odd")

    ulang = input("Do you want to repeat? ")
    print()

print("Program Stops")
print("Thank you for using my program ^^")