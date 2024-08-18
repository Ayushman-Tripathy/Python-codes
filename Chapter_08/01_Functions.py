marks = [71, 59, 70, 61, 54, 91]

percentage = ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5])/600)*100
print(f"Your percentage is: {percentage}")

'''Function is a group of statements performing a specific task .

syntax of a function is 

def function_name():
    print('Hello world')'''

def greet():
    return print('Hello World')
    
greet() 



# def percentage(mark):
#     return ((mark[0] + mark[1] + mark[2] + mark[3] + mark[4] + mark[5])/600)*100
    
# Marklist = []

# for i in range(1,7):
#     num =int(input(f"Enter your {i}'s mark: "))
#     Marklist.append(num)
# percentage1 = percentage(Marklist)
# print(f"Your percentage is: {percentage1}")

# function() ---> this is called calling to a function




def Sum():
    # global one 
    one = int(input('Enter a number: '))
    # global two 
    two = int(input('Enter a number: '))
    plus = one + two
    x = 6 # so x is inside the def (function) and it only can be accessible with this function only
    # to access the value of x or other outside we have to use "global <variable name>"
    global y
    y = 7
    print(plus,x)

Sum()
# print(x)
# print(x) it will throw a error as x is not defined globally inside the above function 
print(y)
# print(y) it won't throw any error as y is global

