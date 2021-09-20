# Get input for marks
# show grade based on the marks
# A 80 and above , B --> 70 and above, C is 50 and above, below 50 is fail
# Invalid marks is more that 100 or below 0
# using elif meaning else if

marks = float(input("Please enter the mark: "))

if marks > 100 or marks < 0:
    grade = 'Invalid'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'Fail'

print("Your grade is ", grade)