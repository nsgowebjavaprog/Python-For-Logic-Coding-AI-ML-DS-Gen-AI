# nested loop
'''
rows = 5
columns = 5
symbol = "*"

for i in range(rows):
    for j in range(columns):
        print(symbol, end=' ')
    print()


#------------------------- Collections

# 1.List --> Ordered, Changeable, Allows Duplicates

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # Output: apple

print(fruits[::2]) # Output: ['apple', 'cherry']
print(fruits[::-1]) # Output: ['cherry', 'banana', 'apple']


for fruit in fruits:
    print(fruit)
    
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

# print(help(fruits))

fruits.insert(1, "orange")
print(fruits)

print("apple" in fruits) # True

fruits.remove("banana")
fruits.append("coconut")
print(fruits)
fruits.sort()

print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
# print(fruits[0]) # IndexError: list index out of range


# Set --> Unordered, Unchangeable, No Duplicates

my_set = {"apple", "banana", "cherry"}
print(my_set)

my_set.add("orange")
print(my_set)

my_set.pop()
print(my_set) # Note: The pop() method removes a random item from the set, as sets are unordered.



# Tuple --> Ordered, Unchangeable, Allows Duplicates

my_tuple = ("apple", "banana", "cherry")
# print(help(my_tuple))

# Top 10 Tuple Operations in One File

my_tuple = ("apple", "banana", "cherry")

# 1. Indexing
print("1. Indexing:", my_tuple[0]) # Output: apple

# 2. Negative Indexing
print("2. Negative Indexing:", my_tuple[-1])

# 3. Slicing
print("3. Slicing:", my_tuple[0:2])

# 4. Length
print("4. Length:", len(my_tuple))

# 5. Check Item Exists
print("5. 'banana' in tuple:", "banana" in my_tuple)

# 6. Count Method
my_tuple2 = ("apple", "banana", "apple")
print("6. Count 'apple':", my_tuple2.count("apple"))

# 7. Index Method
print("7. Index of 'cherry':", my_tuple.index("cherry"))

# 8. Concatenation
new_tuple = my_tuple + ("orange",)
print("8. Concatenation:", new_tuple)

# 9. Repetition
print("9. Repetition:", my_tuple * 2) # values will be repeated twice

# 10. Convert to List and Modify
temp = list(my_tuple)
temp.append("orange") ### we cannot modify tuple but we can convert it to list and modify it and then convert it back to tuple
modified_tuple = tuple(temp)
print("10. Modified Tuple:", modified_tuple)

# Dictionary --> Unordered, Changeable, No Duplicates

# Dictionary --> Unordered, Changeable, No Duplicates

my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# 1. Access Value
print("1. Access:", my_dict["name"])

# 2. Using get()
print("2. Get:", my_dict.get("age"))

# 3. Add New Key-Value
my_dict["email"] = "john@gmail.com"
print("3. After Adding:", my_dict)

# 4. Update Value
my_dict["age"] = 26
print("4. After Update:", my_dict)

# 5. Remove Item using pop()
my_dict.pop("city")
print("5. After Pop:", my_dict)

# 6. Keys()
print("6. Keys:", my_dict.keys())

# 7. Values()
print("7. Values:", my_dict.values())

# 8. Items()
print("8. Items:", my_dict.items())

# 9. Check Key Exists
print("9. 'name' in dict:", "name" in my_dict)

# 10. Clear Dictionary
temp_dict = my_dict.copy()
temp_dict.clear()
print("10. After Clear:", temp_dict)




# 2D List

# # # fruits = ["apple", "orange", "banana", "coconut"]
# # # vegetables = ["carrot", "broccoli", "spinach"]
# # # meats = ["chicken", "beef", "pork"]

# # # grocery_list = [fruits, vegetables, meats]

# # grocery_list = [["apple", "orange", "banana", "coconut"],
# #                 ["carrot", "broccoli", "spinach"],
# #                 ["chicken", "beef", "pork"]]

# # for i in grocery_list:
# #     for j in i:
# #         print(j, end=" ")
# #     print()

# # print(grocery_list[0][1]) # Output: orange

# # 2D List with number pad

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# ------- dictionaries

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "china": "Beijing",
    "Russia": "Moscow"
}
print(capitals)

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "china": "Beijing",
    "Russia": "Moscow"
}
capitals.update({"Japan": "Tokyo"})
print(capitals)

# 1️⃣ Access value using key
print(capitals["India"])
# Output: New Delhi

# 2️⃣ Access value using get()
print(capitals.get("USA"))
# Output: Washington D.C.

# 3️⃣ Get all keys
print(capitals.keys())
# Output: dict_keys(['USA', 'India', 'china', 'Russia'])

# 4️⃣ Get all values
print(capitals.values())
# Output: dict_values(['Washington D.C.', 'New Delhi', 'Beijing', 'Moscow'])

# 5️⃣ Get all key-value pairs
print(capitals.items())
# Output: dict_items([('USA', 'Washington D.C.'), ('India', 'New Delhi'), ('china', 'Beijing'), ('Russia', 'Moscow')])

# 6️⃣ Add new key-value pair
capitals["Japan"] = "Tokyo"
print(capitals)
# Output: Japan added

# 7️⃣ Update value
capitals["India"] = "Delhi"
print(capitals["India"])
# Output: Delhi

# 8️⃣ Remove element using pop()
capitals.pop("china")
print(capitals)
# Output: china removed

# 9️⃣ Remove last inserted item using popitem()
capitals.popitem()
print(capitals)
# Output: last item removed

# 🔟 Check if key exists
print("Russia" in capitals)
# Output: True


capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "china": "Beijing",
    "Russia": "Moscow"
}
# print(capitals)

for key, value in capitals.items():
    print(f"{key}: {value}")
    


# random numbers

import random

# print(random.randint(1, 10)) # random integer between 1 and 10

options = ["A", "B", "C", "D"]
option = random.choice(options)
print(option)

cards = ["2 of Hearts", "3 of Diamonds", "4 of Clubs", "5 of Spades"]
random.shuffle(cards)
print(cards)


import random

lowest = 1
highest = 100

random_number = random.randint(lowest, highest)
# print(random_number)

guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lowest} and {highest}.")

while is_running:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {guesses} guesses.")
            is_running = False
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        
print("Game Over. Thanks for playing!")


'''




