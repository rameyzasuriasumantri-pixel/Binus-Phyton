# Volume of a Cylinder

#INPUT
radius = float(input("Enter the radius (m): "))
height = float(input("Enter the height (m): "))

#PROCESS
pi = 3.14
volume = pi * radius ** 2 * height

#OUTPUT
print(f"The volume of the cylinder is {volume: .2f} m³")