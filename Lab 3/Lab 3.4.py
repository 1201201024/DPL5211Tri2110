hourly_rate = 6.50

# Get input of how many hours worked for a week
# calculate staff salary for one week
# if staff work more that 40 hours, every pay is 10.50 per hour for the additional hours
# Staff can not work 60 hours per week, so only additional 20 hours is calculated for overtime pay
# display the salary

hours = float(input("Hours worked for a week: "))

if hours <= 40:
    salary = hours * hourly_rate
elif hours <= 60:
    salary = 40 * hourly_rate + (hours - 40) * 10.5
else:
    salary = 40 * hourly_rate + 20 * 10.5

print("Salary is {:.2f}.".format(salary))