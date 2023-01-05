""" Given four values representing counts of quarters, dimes, nickels, and pennies,
Output the total amount as dollars and cents.
Output each floating point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}') Ex. If the input is: 4 3 2 1
where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels,
and 1 is the number of pennies, the output is: Amount:$1.41. For simplicity, assume the input is a non-negative number.
"""
quarters = int(input("Enter number of Quarters: "))
dimes = int(input("Number of Dimes: "))
nickels = int(input("Number of Nickels: "))
pennies = int(input("Number of Pennies: "))

Amount = quarters * float(0.25) + dimes * float(0.10) + nickels * float(0.05) + pennies * float(0.01)
#Prints out Amount within two decimal places.
print('Amount: ${:.2f}'.format(Amount))

