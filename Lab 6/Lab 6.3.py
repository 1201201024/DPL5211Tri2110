with open("demofile.txt", "r") as f:
    data = f.readlines()
    for line in data:
        words = line.split(",")
        print(words)
f.close()