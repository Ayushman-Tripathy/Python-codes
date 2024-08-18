mark1 = int(input("Enter the mark of subject 1: "))
mark2 = int(input("Enter the mark of subject 2: "))
mark3 = int(input("Enter the mark of subject 3: "))

total = (mark1 + mark2 + mark3) / 3

# if (mark1>33):
#     if (mark2>33):
#         if (mark3>33):
#             if (total>40):
#                 print ("Yes your pass!")
# else:
#     print("Fail")

#  OR 

if (mark1<33 or mark2<33 or mark3<33):
    print ("Your failed in the Examination Due to less than 33%")

elif (total<40):
    print ("You are failed in the examination due to less than 40%")
else :
    print("Congrats! You are passed the examination")