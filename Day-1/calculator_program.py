opearator = input("Enter operator: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if opearator == "+":
    print(num1 + num2)
elif opearator == "-":
    print(num1 - num2)
elif opearator == "*":
    print(num1 * num2)
elif opearator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")