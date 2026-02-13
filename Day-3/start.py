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


'''

