name = input("What's your name? ")
print(f"Hello, {name}!")

#All data that is entered is converted to a string.
price = input("How much for the truck? ")
price = float(price)
if price < 10000:
 print("I'll take it.")