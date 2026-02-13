unit = input("Celsius or Fahrenheit (c or f)")
temperature = float(input("Enter the temperature: "))

if unit == "c":
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature} degrees Celsius is equal to {converted_temperature} degrees Fahrenheit.")
    
elif unit == "f":
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature} degrees Celsius.")
    
else:
    print("Invalid unit. Please enter 'c' or 'f'.")