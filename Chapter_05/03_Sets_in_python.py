# Set is a collection of non-repetitive elements 
# A set is a collection which is unordered, unchangeable*, and unindexed.



'''  We can assign a set with {}
EX- syntax abc = {1,2,3,4}
or abc = set(1,2,3,4) '''

a = {}
print(type(a))
''' Important- The syntax will create a
empty dictionary not a empty set '''

'''To create a empty set, 
we have to use the below syntax'''
b = set()
print(type(b))

# As duplicate values are not allowed 
# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
# and first one is assigned and the second value which is duplicate is not added as its a dupe 


thisset1 = set(("apple", "banana", "cherry"))
print(thisset1)
# Note: the set list is unordered, so the result will display the items in a random order.


thisset2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset2.update(tropical)

print(thisset)