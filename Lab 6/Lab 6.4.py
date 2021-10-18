def get_average(words):
    for num in words:
        # get the number of sales
        # get the total
        total += float(num)

with open("sales.txt", "r") as f:
    data = f.readlines()
    for line in data:
        words = line.split(",")

average = get_average(words)