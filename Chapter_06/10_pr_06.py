print ("Hello !\ni will help you to find your Grade")
persentage = int(input("Enter your persentage: "))

if (persentage<=100 and persentage>=90):
    print("Your grade is Ex")
elif (persentage<=89 and persentage>=80):
    print("Your grade is A")
elif (persentage<=79 and persentage>=70):
    print("Your grade is B")
elif (persentage<=69 and persentage>=60):
    print("Your grade is C")
elif (persentage<=59 and persentage>=50):
    print("Your grade is D")
elif (persentage<=49 and persentage>=0):
    print("Your grade is Fail")
else:
    print("Your input is wrong please try again")
