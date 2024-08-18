def greatest_of_three(num1, num2, num3):
    if (num1>num2):
       if (num1>num3):
           return num1 
       else:
           return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

sasta_list = []
for i in range(1,4):
    num = int(input("Enter a number: "))
    sasta_list.append(num)

g = greatest_of_three(*sasta_list)
print(g)
