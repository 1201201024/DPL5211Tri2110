# Lab 4.5.py get input for a number from 1 until 12 using the for loop display the multiplication tables

num = int(input("Enter the number from 1 to 10 : "))

for i in range(1, 13):
    print(num, "x", i, "=", num * i)