balance = int((input("Enter your balance: ")))

new_balance = '${:,}'.format(balance)

print("Your updated balance: {0}".format(new_balance))