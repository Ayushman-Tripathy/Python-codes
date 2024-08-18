# So first let's Create a set 
Sipun = {1,2,3}

# print the new set which one we just created 
print (Sipun)


# METHODS FOR SET

# we can add elements into the Sipun set by .add
Sipun.add(4)
Sipun.add(5)
Sipun.add(6)
Sipun.add(6)
Sipun.add(6)
Sipun.add(6)  # Adding a same value Dosn't
Sipun.add(6)  # change anything in the set

# print (Sipun)

# Sipun.add([7,8]) Throws a error 
# Sipun.add({7:8}) Throws a error

''' We can't add a List or Dictionary inside a
set because we can change the value of the 
List or Dictionary but we can't change the set '''

# We can add Only immutable types of data (hassable type)

Sipun.add((7,8))
# We can add a tuple inside a set because its hassable/immutable

# print (len(Sipun))
# Prints the length of this set, i.e.-7 rn and the tuple is counted as a single element

# Sipun.discard(6) same as below
Sipun.remove(6)
# Used to remove a element in the given set
# Sipun.remove(100) Throws a error while trying to remove 100 as it's not present in the set 

print(Sipun.pop())
# Used to print and remove a random element from the given set
print(Sipun)

Sipun.clear()
# Used to clear out given set
print(Sipun)

a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9, 0}
print(a.union({7,8}))
print(a)
# It will print a new set {1,2,3,4,7,8}

print(a.intersection({3,4}))
print(a)
# It will print a new set {3,4}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

e = a.symmetric_difference(b)
print(e)

