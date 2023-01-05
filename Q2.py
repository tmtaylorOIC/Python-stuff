"""Write a program whose inputs are three integers,
and whose output is the smallest of the three values.
Ex. If the input is: 7  15  3, the expected output should be 3."""
# This reads the three integers that are input by the user.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

#If num1 is less than num2 and num3 then print num1 is the smallest number.
if num1 < num2 and num1 < num3:
    print("The smallest number is: ", num1)

#If num2 is less than num1 and num3 then print num1 is the smallest number.

elif num2 < num1 and num2 < num3:
    print("The smallest number is: ", num2)

#If num3 is less than num1 and num2 then print num1 is the smallest number.
elif num3 < num1 and num3 < num2:
    print("The smallest number is: ", num3)