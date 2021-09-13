PRICE = 0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------\n")
litre = int(input("Enter amount of litres: "))
print("\nPrice per litre \t = RM {:.2f}".format(PRICE))
print("Number of liters \t = {}".format(litre))
total = litre * PRICE
print("Total: RM {:.2f}".format(total))