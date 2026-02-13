weight = float(input("Enter the weight in pounds: "))
unit = input("Kg / pounds (kg or p): ")

if unit == "kg":
    converted_weight = weight * 2.205
    print(f"{weight} pounds is equal to {converted_weight} kilograms.")
elif unit == "p":
    converted_weight = weight / 2.205
    print(f"{weight} pounds is equal to {converted_weight} grams.")
else:
    print("Invalid unit. Please enter 'kg' or 'g'.")