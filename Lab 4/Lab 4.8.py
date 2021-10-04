# Lab 4.8.py Given an array of 3, 6, 9, 12, 23 create another array containing the squared number of each number
# from the first array and display the second array

num = [3, 6, 9, 12, 23]
square = []

for i in range(0, 5):
    square.append(num[i] * num[i])
    print(square[i])