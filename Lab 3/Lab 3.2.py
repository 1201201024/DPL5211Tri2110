cur_balance = 30.12

# get input from user to withdraw money
# if balance is less RM 10, alert the user that there is no sufficient fund.
# and display the current balanced
# use else: to of the current balance is sufficient and
# display the new current balance.

withdraw = float(input("Please enter the withdraw amount: "))

new_balance = cur_balance - withdraw

if new_balance < 10:
    print("Insufficient fund")
    print("Your current balance is: {:.2f}".format(cur_balance))
else:
    print("Sufficient balance")
    print("New current balance is: {:.2f}".format(new_balance))