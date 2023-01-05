"""Given a long integer representing a 10-digit phone number,
output the area code, prefix,
and line number using the format (800)555-1212. Ex. If the input is:
8005551212. Hint: Use % to get the desired rightmost digits."""

num = int(input("Enter 10-digit number without dashes (-): "))

#Use modulo (%) to get the right most digits. Divide the phone number by 10000 and the remainder is 1212.
last_four = num % 10000

#Use floor division (//) to drop the last 4 from the original phone number.  800555 should be all that remains.
num = num // 10000

#Use modulo to get the prefix (middle 3 numbers): 555
prefix = num % 1000

#Use floor division to drop the prefix from num and save as area_code: 800
num = num // 1000
area_code = num % 1000

print("The phone number is: ({})-{}-{}".format(area_code, prefix, last_four))
