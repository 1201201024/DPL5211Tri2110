# Lab 4.2.py: Create a while loop that displays even numbers from 10 until 2
# 10, 8, 6, 4, 2

start = 10
while (start >= 2):
    if (start % 2 == 0):
        print(start, end=" ")
    start = start - 1