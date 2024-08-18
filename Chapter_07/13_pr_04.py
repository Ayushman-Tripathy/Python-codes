number = int(input("Enter your number: "))

for i in range(2,number):
    if(number % i == 0):
        print(number,"is not a prime number")
        break
    if(number % i != 0):
        print(number,"is a prime number")
        break



# number = int(input("Enter your number: "))
# prime = True

# for i in range(2,number):
#     if(number % i == 0):
#         prime = False
#         break    

# if prime:
#     print(number,"is a prime number")
# else:
#     print(number,"is not a prime number")