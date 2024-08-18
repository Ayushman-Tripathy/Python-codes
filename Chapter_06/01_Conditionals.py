# # 1. if-elif-else LADDER IN PYTHON 

# a = 10
# if (a>14):
#     print ("The Value of a is Greater than 14")
# elif (a>13):
#     print ("The Value of a is Greater than 13")
# elif (a>12):
#     print ("The Value of a is Greater than 12")
# elif (a>11):
#     print ("The Value of a is Greater than 11")
# elif (a>10):
#     print ("The Value of a is Greater than 10")
# elif (a>9):
#     print ("The Value of a is Greater than 9")
# else:
#     print ("The value of a is:",a)



# # 2. MULTIPLE if STATEMENTS 

# a = 10
# if (a>7):
#     print ("The Value of a is Greater than 7")
# if (a>8):
#     print ("The Value of a is Greater than 8")
# if (a>9):
#     print ("The Value of a is Greater than 9")
# if (a>10):
#     print ("The Value of a is Greater than 10")
# # if (a>=10):               WE CAN WRITE LIKE THIS TOO
#     # print ("The Value of a is Greater than 10")
# else:
#     print ("The value of a is:",a)



# # NESTED if STATEMENT 

# a = 10 
# if (a>6):
#     print("The value of a is greater than 6")
#     if (a>7):
#         print("The value of a is greater than 7")
#         if (a>8):
#             print("The value of a is greater than 8")
#             if (a>9):
#                 print("The value of a is greater than 9")
#                 if (a>10):
#                     print("The value of a is greater than 10")
#                 else:
#                     print("The value of a is 10 or above")


''' IMP NOTE-
 1. THERE CAN BE ANY NUMBER OF elif CONDITIONS IN A if-else LADDER
 2.LAST else IS EXECUTED ONLY IF ALL THE CONDITIONS INSIDE OF elifS
   FASLE. 
    (*. ELSE CONDITION IS OPTIONAL) '''                    
 
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
