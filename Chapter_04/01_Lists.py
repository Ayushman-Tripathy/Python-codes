''' Python Lists are containers to store a set of 
values of any data type '''
# List items are ordered, changeable, and allow duplicate values.
# We can assign a List by []

Any = [1, 2, 3, 4, 5, 6]

# We can print a List by print() function
print(Any)

# We can access using index by Any[0], Any[1], Any[3]
print(Any[2])

# We can create a List with items of different types 
Mix = [1, "Hello", 5.0, True]
print(Mix)

# We can modify / (changethe value of) a List by Any[0] = "modified"
Any[0] = "modified"
print(Any[0])

# WE CAN UPDATE LISTS ANYTIME EVEN AFTER ASSINGING THE VALUES 

L1 = [] # It's a Empty List 
L2 = [1,] # It's a List with single element 

print (L1)
print (L2)

# ADD LIST ITEMS 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)

# REMOVE FROM LIST

# By pop and del

# thislist.pop(0)
# del thislist[0]

# We can use remove too 

# thislist.remove("apple")

# clear a list
# thislist.clear()  # used to clear a list but list still present with no content (empty list)

# del thislist
# print(thislist) # It will throw a error because the list already deleted 

# We can add two list too 
list1 = ['harry', 'ram', 'syam', 'ayush', 'sipun']
list2 = [1, 2, 3, 4, 5]
list3 = list1 + list2
print(list3)

# We can copy a list too
# With
# new_list1 = list1 
# Or with
# new_list1 = list1.copy()
# Or with list method
# new_list1 = list(list2)

# print(new_list1)
# print(new_list1)