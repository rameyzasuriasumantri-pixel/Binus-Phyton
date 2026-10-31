def grade_point(grade):
    if grade == "A":
        return 4.00
    elif grade == "A-":
        return 3.75
    elif grade == "B+":
        return 3.50
    elif grade == "B":
        return 3.00
    elif grade == "B-":
        return 2.75
    elif grade == "C+":
        return 2.50
    elif grade == "C":
        return 2.00
    elif grade == "C-":
        return 1.75
    elif grade == "D":
        return 1.50
    else:
        return 1.20


total = 0
jumlah = 0

grade = input("Enter Grade Category (Press Enter to Stop): ")

while(grade != ""):
    total = total + grade_point(grade)
    jumlah = jumlah + 1
    grade = input("Enter Grade Category (Press Enter to Stop): ")

rata = total / jumlah

if rata >= 4.00:
    huruf = "A"
elif rata >= 3.75:
    huruf = "A-"
elif rata >= 3.50:
    huruf = "B+"
elif rata >= 3.00:
    huruf = "B"
elif rata >= 2.75:
    huruf = "B-"
elif rata >= 2.50:
    huruf = "C+"
elif rata >= 2.00:
    huruf = "C"
elif rata >= 1.75:
    huruf = "C-"
elif rata >= 1.50:
    huruf = "D"
else:
    huruf = "E"

print(f"The average grade is {rata:.2f} with a designation of {huruf}")