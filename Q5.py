""" Given two input integers: one for the arrow's body and one for the arrow's head,
print a right-facing arrow. If the input is: 0 1 There are five spaces preceding row one and row 5. There
are no spaces preceeding rows 2, 3, and 4."""

body = input()
head = input()

row1 = "     " + head 
row2 = body * 5 + head * 2
row3 = body * 5 + head  * 3

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)
