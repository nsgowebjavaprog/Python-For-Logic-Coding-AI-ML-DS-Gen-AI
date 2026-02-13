# Logical operators:
'''
# and operator:
age = 25
if age > 18 and age < 30:
    print("You are eligible for the job.")
    
# or operator:
age = 25
if age < 18 or age > 30:
    print("You are not eligible for the job.")

# not operator:
age = 25
if not age < 18:
    print("You are eligible for the job.")


# --------------------- Conditional statements:

num = 5

print("+ve" if num>0 else "-ve")

print("Even" if num % 2 == 0 else "Odd")



# --------------------- Strings-Methods:

name = input("Enter the full name: ")
print(len(name))

print(name.find(" ")) # Finds the index of the first occurrence of a space in the name. If there is no space, it will return -1.

print(name.upper()) # Converts the name to uppercase.

print(name.lower()) # Converts the name to lowercase.

print(name.title()) # Converts the first letter of each word in the name to uppercase and the rest to lowercase.

print(name.strip()) # Removes any leading and trailing whitespace from the name. If there is no whitespace, it will return the name as it is.


print(name.replace(" ", "_")) # Replaces all occurrences of a space in the name with an underscore. If there is no space, it will return the name as it is.

print(name.split(" ")) # Splits the name into a list of words based on the space character. If there is no space, it will return a list with the name as the only element.

print(name.startswith("A")) # Checks if the name starts with the letter "A". If it does, it will return True, otherwise it will return False.

print(name.endswith("a")) # Checks if the name ends with the letter "a". If it does, it will return True, otherwise it will return False.

print(name.isdigit()) # Checks if the name consists of only digits. If it does, it will return True, otherwise it will return False.

print(name.isalpha()) # Only checks for alphabets, if there is a space it will return False.

print(name.count("a")) # Counts the number of occurrences of "a" in the name.


print(help(str))


user_name = input("Enter your name: ")

if len(user_name) > 12:
    print("Your name is too long.")

elif user_name.find(" ") != -1:
    print("Your name should not contain spaces.")

elif any(char.isdigit() for char in user_name):
    print("Your name should not contain digits.")

else:
    print("Your name is valid.")
    


# --------------------- Indexing and slicing: [start : end : step]

create_number = "1234-5678-9012-3456"

print(create_number[0]) 

last_four_digits = create_number[-4:]
print(last_four_digits)

last_four_digits_reversed = create_number[-1:-5:-1]
print(last_four_digits_reversed)

last_one = create_number[-1]
print(last_one)

create_number = "1234-5678-9012-3456"

print(create_number[0])      # 1
print(create_number[1])      # 2
print(create_number[4])      # -
print(create_number[-1])     # 6
print(create_number[-4])     # 3

print(create_number[0:4])    # 1234
print(create_number[5:9])    # 5678
print(create_number[10:14])  # 9012
print(create_number[15:19])  # 3456

print(create_number[:4])     # 1234
print(create_number[5:])     # 5678-9012-3456
print(create_number[-4:])    # 3456
print(create_number[:-5])    # 1234-5678-9012

print(create_number[::2])    # Every 2nd character
print(create_number[1::2])   # Every 2nd character from index 1
print(create_number[::-1])   # Reverse string
print(create_number[::3])    # Every 3rd character

print(create_number[5:9:2])  # 5 to 9 step 2
print(create_number[0:19:4]) # Step 4
print(create_number[-19:-15])# First 4 digits using negative slicing


# --------------------- Format specifiers:

price_1 = 3.14159
price_2 = -987.65
price_3 = 12.34

print(f"Price 1: {price_1:.2f}") # 2 decimal places
print(f"Price 2: {price_2:10}") # 10 characters wide, right-aligned
print(f"Price 2: {price_2:010}") # 10 characters wide, right-aligned, zero-padded
print(f"Price 2: {price_2:<10}") # 10 characters wide, left-aligned
print(f"Price 2: {price_2:>10}") # 10 characters wide, right-aligned

print(f"Price 2: {price_2:^10}") # 10 characters wide, centered
print(f"Price 1: {price_1:+}") # Show the sign for positive numbers


# --------------------- While loop:

age = -2

while age < 0:
    print("Invalid age. Please enter a non-negative number.")
    age = int(input("Enter your age: "))
    
print("Your age is valid.")

'''

# --------------------- For loop:

for i in range(1, 11):
    
    if i == 5:
        break
    else:
        print(i) # 1 to 4