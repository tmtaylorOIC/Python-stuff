""" A palindrome is a word or a phrase that is the same when read both forward and backward.
Examples are: "bob", "sees", or "never odd or even"(ignoring spaces). Write a program whose input is a word or a phrase, and that
outputs whether the input is a palindrome. Ex. If the input is: bob
The output is: bob is a palindrome.""" 

#Pronmpt user input
user_input = input("Input word: ")
#get the reverse of the input and save it to variable
reverse = user_input[::-1]
#compare the variables 
if user_input == reverse:
    print("{} is a palindrome".format(user_input))
else:
    print("{} is not a palindrome".format(user_input))
