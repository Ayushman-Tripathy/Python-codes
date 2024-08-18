'''IN A DICTIONARY KEYS CAN'T BE SAME/DUPLICATE 
IF WE PROVIDE SAME KEY AGAIN THE VALUE OF 
THE KEY WILL REPLACED BY THE LASTLY 
EXECUTED KEY'S VALUE'''

''' Q7- IF NAME OF 2 FRIENDS ARE SAME; 
 WHAT WILL HAPPEN TO THE PROGRAM IN PROBLEM 6 ? '''
#  PRINTING THE PROBLEM 6 HERE
FavLanguage = {}

a = input("Ayushman enter your Favourate Language:")
b = input("Leslie enter your Favourate Language:")
c = input("Vijay enter your Favourate Language:")
# d = input("Swadhin enter your Favourate Language:")
# Changing the name swadhin to Leslie 
d = input("Leslie enter your Favourate Language:")

FavLanguage["Ayushman"] = a           #Python
FavLanguage["Leslie"] = b             #Java
FavLanguage["Vijay"] = c              #C
# FavLanguage["Swadhin"] = d          #C++
# Changing the name swadhin to Leslie 
FavLanguage["Leslie"] = d             #First Java but after this line its C++

print(FavLanguage)

##ANS- IF THERE ARE 2 FRIENDS WITH SAME NAME THEN THE FIRST VALUE 
# OF THE NAME WILL REPLACED BY THE SECOND VALUE OF THE SAME NAME  
