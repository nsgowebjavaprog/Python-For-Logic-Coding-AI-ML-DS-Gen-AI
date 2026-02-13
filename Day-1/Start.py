'''
#---------------------------variables---------------------------------
# variables:- Store the value.

# String
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

# Integer
age = 25
quantity = 3

print(f"You are {age} years old")
print(f"You are buying {quantity} items")

# float
price = 10.99
cgpa = 9.50
print(f"The price is ${price}.")
print(f"Your cgpa is: {cgpa}")

# boolean
is_student = True
is_graduate = False

print(f"Are you a Student: {is_student}.")
print(f"Are you a Graduate: {is_graduate}.")
'''
#-----------------------------Type-Casting-------------------------------
'''
name = "Code"
age = 25
cgpa = 9.45
is_student = True

print(type(name))

cgpa = int(cgpa)
print(cgpa)

age = float(age)
print(type(age))  # float

name = bool(name)
print(name) # bool  # True

age = str(age)
print(type(age))  # 25.0   # str
'''
#-----------------------------User-Input-------------------------------
# input() --> Fuction and retrun String data as default
'''
name = input("Enter the user name:")
age = int(input("Enter the Age"))

print("My name is: ", name)
print(f"I am {age} years old.")


# Ex-1 Reactangle Area Calc

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width

print(f"The are is: {area} cm²")

# E.x-2 Shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is price "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"price is: {price}, and quantity is: {quantity} then Total is: ${total}")
'''

## 6   arithmetic & math 📐
'''
frds = 5
print(frds)

frds += 5
print(frds)

frds /= 5
print(frds)

frds **= 2
print(frds)

remender = 10 % 3
print(remender)

a = 3.14
b = -4
c = 5

res1 = round(a)
print(res1)

res2 = abs(b)
print(res2)

res3 = pow(2,5)
print(res3)

res4 = max(a,b,c)
print(res4)

# min

import math

print(math.pi)

print(math.e)

res1 = math.sqrt(3)
print(res1)

print(math.ceil(9.2)) # 10

print(math.floor(9.2)) # 9


# 2 * pi * r

import math

print(2 * math.pi * 10)
print(math.pi * pow(10,2))
'''

## 7   if statements 🤔
'''
# 1
age = int(input("Enter the age: "))

if age >= 18:
    print("You are now eligible")
elif age < 0:
    print("-ve")
else:        
    print("Not eligible")
    
# 2
response = input("Enter the food? [Y/N]: ")

if response == "y":
    print("Uta")
else:
    print("Still time is there")        
'''
