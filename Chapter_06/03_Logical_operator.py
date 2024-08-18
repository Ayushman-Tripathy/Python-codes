# Logical Operators works with 1 or 2 operands and returns a boolean value, i.e- true or false 

# # First logical operator is- "and" (It operates with 2 operands)
# age = int(input("Enter your age: "))
# if(age>=20 and age<=32):
#     print("Congrats !!!\n\tYou can Join us !")
# else:
#     print("You can't join here")
# # the "and" returns true if both the conditions are true else false


# # Second logical operator is- "or" (It operates with 2 operands)
# age1 = int(input("Enter your age: "))
# if(age1<=15 or age1<=20):
#     print("Nice you are perfect!")
# else:
#     print("Sorry we can't accept you")
# # the "or" returns true if atleast one of the statement is true else false 


# Third logical operator is- "not" (It operates with only 1 operand)
age2 = int(input("Enter your age: "))
if (not age2<=0):
    print("It is a valid input")
else:
    print("It is not a valid input")
# the "not" returns the opposite of the statement true -> false and false -> true
