BANANA = 1.5
GRAPE = 5.6

print("Invoice for Fruits Purchase")
print("---------------------------------\n")
comb = int(input("Enter the quantity (comb) of bananas bought : "))
kg = int(input("Enter the amount (kg) of grapes bought : "))
print("\nItem \t\t Qty \t Price \t\t Total")
BananaTotal = comb * BANANA
print("Banana (combs) \t {} \t RM{:.2f} \t {:.2f}".format(comb, BANANA, BananaTotal))
GrapeTotal = kg * GRAPE
print("Grapes (kg) \t {} \t RM{:.2f} \t {:.2f}".format(kg, GRAPE, GrapeTotal))
print("\t")
print("Total: RM{:.2f}".format(BananaTotal + GrapeTotal))
