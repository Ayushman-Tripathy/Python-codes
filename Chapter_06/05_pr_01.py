num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))
num4 = int(input("Enter the number 4: "))

if (num1>num2):
    r1 = num1
else:
    r1 = num2

if (num3>num4):
    r2 = num3
else:
    r2 = num4

if(r1>r2):
    print (r1, "Is the greatest number")
else:
    print (r2, "Is the greatest number")
    