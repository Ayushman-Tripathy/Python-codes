# string = "This  is a String containg double spaces "
string = input("Enter a String:\n")
DoubleSpaces = string.find("  ")

print (DoubleSpaces)

if DoubleSpaces > -1:
    print ("There is some double spaces in",DoubleSpaces)
    question = input ("Want to remove the Double spaces ? ans with y/n ")
    if question.lower() == 'y':
        string = string.replace ("  "," ")
else: print ("There is no Double spaces in it :)")

# test = string.find("  ")
# print (test)     
print (string)
# if string == -1:
#     print ("The all Double spaced are removed successfully :D")
print ("congrats the double space removed successfully :D")
