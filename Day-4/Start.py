# Function:- a block of code which only runs when it is called. It can take inputs and return outputs.
'''
def function_name(parameters):
    code to execute
function_name(arguments)


def fun_helllo(name):
    # pass
    print("Hello World", name)

fun_helllo("NS")


def creating_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = first_name + " " + last_name
    return full_name
name = creating_name("nS", "s")
print(name)



# Default arguments

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)
print(net_price(1000, 0.4)) # Consider 0.4 as discount.


# keywords arguments

def greet(name, greeting, punctuation):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice", "Hello", "!")  # Positional arguments
greet(name="Bob", greeting="Hi", punctuation=".")  # Keyword arguments


#   *args [arguments] -            allows a function to accept any number of positional arguments as a tuple.
#   **kwargs [Keyword arguments] - allows a function to accept any number of keyword arguments as a dictionary.

def sum_all(*args): # args == any name 
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3, 4, 5))  # Output: 15    



def print_adr(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_adr(name="Alice", city="New York", country="USA")

'''
