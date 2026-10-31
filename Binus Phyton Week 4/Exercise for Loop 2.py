max_value = int(input("Input Max Value: "))
print()

for i in range(max_value, 0, -1):
    baris = ""
    for j in range(i):
        baris = baris + str(i)
    print(baris)

for i in range(2, max_value + 1):
    baris = ""
    for j in range(i):
        baris = baris + str(i)
    print(baris)