# Shoping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food / q for quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price: "))
        foods.append(food)
        prices.append(price)

print("-----Your shopping cart-----")

for food in foods:
    if food == foods[-1]:
        print(food)
    else:    
        print(food, end=", ")

for price in prices:    
    total += price

print(f"Total: {total}")