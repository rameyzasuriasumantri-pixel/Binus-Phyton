numbers = []

#INPUT : read 5 numbers, one at a time
for i in range(5):
  num = float(input(f"Enter number{i+1}"))
  numbers.append(num)
  
#PROCESS: sort the list
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

#OUTPUT
print("Ascending sorted list:", ascending)
print("Descending sorted list:", descending)
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))