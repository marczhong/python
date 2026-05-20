# total amount in the bank
total = 10000

# input password
password = input("Enter your password:")
print(f"Password correct!, {password}")

# input amount to withdraw
amount = input("Enter the amount to withdraw:")

# calculate remaining balance
print(f"Remaining balance: {total - int(amount)}")

