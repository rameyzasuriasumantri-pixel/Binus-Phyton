#Age Category

#INPUT
age = int(input("Enter your age: "))

#PROCESS and OUTPUT
if age < 0:
  print("Age cannot be negative")
elif age <= 1:
  print("Category: Baby")
elif ((age >=2) and (age <=3)):
  print("Category: Toddler")
elif ((age >= 4) and (age <= 5)):
  print("Category: Preschooler")
elif ((age >= 6) and (age <= 12)):
  print("Category: Child")
elif ((age >= 13) and (age <= 17)):
  print("Category: Teenager")
elif ((age >= 18) and (age <= 21)):
  print("Category: Young Adult")
elif ((age >= 22) and (age <= 30)):
  print("Category: Pre-adult")
elif ((age >= 31) and (age <= 50)):
  print("Category: Adult")
elif ((age >= 51) and (age <= 70)):
  print("Category: Pre-elderly")
else:
  print("Category: Elderly")