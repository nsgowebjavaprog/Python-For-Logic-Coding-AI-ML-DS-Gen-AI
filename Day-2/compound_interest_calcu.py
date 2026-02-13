# Compound Interest Calculator

# formula = A = P(1 + r/n)^(nt)

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than 0. Please try again.")
        
while rate <= 0:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")
        
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than 0. Please try again.")
 
print(f"{principal} | {rate}| {time}")       
# Convert annual interest rate from percentage to decimal

rate = rate / 100
# Calculate the compound interest
amount = principal * (1 + rate) ** time
# Display the result

print(f"The amount after {time} years is $: {amount:.2f}")