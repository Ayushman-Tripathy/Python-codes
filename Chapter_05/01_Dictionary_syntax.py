# Dictionary is a collection of KEY-VALUE pairs 
# We can assign values as a dictionary by {}

MyDict = {
    "mithulu" : "Mithu Mithu",
    "mithulu eats" : {
        "mirchi" : "80%",
        "tomato" : "30%",
        "jamba" : "90%"
    },

    "paunlu" : "paunll paunll",
    "tota pila" : "aaww aaww",
    "tingri" : "vacum cleaner"
}
print (MyDict)
print (MyDict["mithulu"])
print (MyDict["mithulu eats"])
print (MyDict["mithulu eats"]["mirchi"])

'''IN A DICTIONARY KEYS CAN'T BE SAME/DUPLICATE 
IF WE PROVIDE SAME KEY AGAIN THE VALUE OF 
THE KEY WILL REPLACED BY THE LASTLY 
EXECUTED KEY'S VALUE'''

'''IN A DICTIONARY THE VALUES OF 2 OR MORE KEYS CAN 
CONTAIN SAME/DUPLICATE '''


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
