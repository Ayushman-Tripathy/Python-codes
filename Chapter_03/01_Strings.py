# String is a Data type in python 
# String is a sequence of characters enclosed in quotes '', "",'''''' . 
a = "Ayushman's"        # Double quote used to use single quote inside a string   
b = 'Tripathy"s'        # Single quote used to use Double quote inside a string
c = '''Ayushman's
Ayushman"s'''    #Triple quote used to use single ,double and next line inside a string 
print(a)
print(b)
print(c)
# print(type(a))

# we can assign values like this also
x, y, z =  "Ayush", "man", "Tripathy"
print(x+y, z)

# we can assign 2 variables with same values
acha = good = "me"


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))
