"""Write a program with the total change amount in pennies as an integer input, and output the change
using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes,
Nickels, and Pennies. Use singular and plural coint names as appropriate, like 1 Penny vs. 2 Pennies.
Ex. If the input is: 0 The output is: No change.
If the input is: 45 the output is: 1 Quarter 2 Dimes"""

#Prompt user to input value
change_in_pennies = int(input("Enter number of penies: "))

#Defin output 
dollar = change_in_pennies // 100
quarter = change_in_pennies % 100 // 25
dime = change_in_pennies % 100 // 10
nickel = change_in_pennies % 100 // 5
penny = change_in_pennies

if change_in_pennies == 0:  #if input equals 0
    print("No Change")  #print "No change"
elif dollar == 1:  #if number of dollars is equals one
    print(dollar, "Dollar")  #print number of dollars (singular)
elif dollar > 1: #if number of dollars is greater than one
    print(dollar, "Dollars") #print number of dollars
if quarter == 1:
    print(quarter, "Quarter")
elif quarter > 1: 
    print(quarter, "Quarters")
if dime == 1:
    print(dime, "Dime")
elif dime > 1: 
    print(dime, "Dimes")    
if nickel == 1:
    print(nickel, "Nickel")
elif nickel > 1: 
    print(nickel, "Nickels")    
if penny == 1:
    print(penny, "Penny")
elif penny > 1: 
    print(penny, "Pennies")