# Temperature Conversion 

# MENU
print("=== Temperature Conversion ===")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

# INPUT
choice = int(input("Choose an option (1-6): "))

match choice:
    case 1:
        temp = float(input("Enter the temperature (°C): "))
        print(f"{temp} °C = {(temp * 9 / 5) + 32:.2f} °F")
    case 2:
        temp = float(input("Enter the temperature (°C): "))
        print(f"{temp} °C = {temp + 273.15:.2f} K")
    case 3:
        temp = float(input("Enter the temperature (°F): "))
        print(f"{temp} °F = {(temp - 32) * 5 / 9:.2f} °C")
    case 4:
        temp = float(input("Enter the temperature (°F): "))
        print(f"{temp} °F = {(temp - 32) * 5 / 9 + 273.15:.2f} K")
    case 5:
        temp = float(input("Enter the temperature (K): "))
        print(f"{temp} K = {temp - 273.15:.2f} °C")
    case 6:
        temp = float(input("Enter the temperature (K): "))
        print(f"{temp} K = {(temp - 273.15) * 9 / 5 + 32:.2f} °F")
    case _:
        print("Invalid option")