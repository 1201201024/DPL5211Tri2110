kilo = float(input("Please enter the value of kilogram :"))
gram = kilo * 1000
# print("For ", kilo, " kilogram is equivalent to ", round(gram, 2), " gram")
print("For {:.2f} kilogram is equivalent to {:.2f} gram".format(kilo, gram))