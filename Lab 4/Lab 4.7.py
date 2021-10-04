# Display the student names in reverse order studnames[0] = "Law Qian Er", studnames[2] "Khoo Chong Qin"

studnames = ["Law Qian Er", "Wong Bing Jie", "Khoo Chong Qin"]

# for name in reversed(studnames):
# for name in studnames[::-1]:
#     print(name)

for studnindex in range(2, -1, -1): # 2, 1, 0
    print(studnames[studnindex])

# studnames.reverse ...reverse list
# studnames.append ...to add a new value
# studnames.remove ...to remove the value