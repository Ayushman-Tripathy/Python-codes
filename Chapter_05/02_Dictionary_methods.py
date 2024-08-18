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

# DIctionary Methods 

print (MyDict.keys())
# Prints the KEYS of the Dictionary

print (MyDict.values())
# Prints the VALUES of the Dictionary

# print (type(MyDict.keys()))
# print (type(MyDict.values()))

# print (list(MyDict.keys()))
# Converting the 'dict_keys' to List

# print (list(MyDict.values()))
# Converting the 'dict_values' to List

print (MyDict.items())
# Prints the (KEYS,VALUES) for all Contents of the Dictionary
updateDict = {
    "New key" : "New value",
    "Dibakar" : "Friend",
    "Bedant" : "Friend",
    "Swadhin" : "Friend"
}

print (MyDict)
MyDict.update (updateDict) #Updates the dictionary by adding Key-Value pairs from updateDict
print (MyDict)

# print (MyDict.get("mithulu")) Used to print the value of "mithulu" key 
# print (MyDict["mithulu"]) Used to print the value of "mithulu" key 

# The difference between .get and [] syntax is 
print (MyDict.get("mithululu")) # It returns None because the mithululu is not presents in the MyDict Dictionary
print (MyDict["mithululu"]) # It throws a error as the mithulu is not presents in the MyDict Dictionary

