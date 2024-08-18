letter = '''Hello dear name ,
You are SELECTED !
Date: date'''

name = input ("Enter Your Name: ")
date = input ("Enter Date: ")

letter = letter.replace("name",name)
letter = letter.replace("date",date)

# we must use  string = string.replace() command to change 
# any input inside a string when that is executed by user 

print (letter)