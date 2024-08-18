# Let's make a list
Numbers = [54, 10, 43, 32, 21, 0]

# list Methods
 
Numbers.sort()  
# It sorts the List in ascending order
# [54, 10, 43, 32, 21, 0]
# [0, 10, 21, 32, 43, 54]

Numbers.reverse()
# It reverses the list like [0, 21, 32, 43, 10, 54]
# [54, 10, 43, 32, 21, 0]
# [0, 21, 32, 43, 10, 54]

Numbers.append('added')
# It addes the given data at the end of the List 
# [54, 10, 43, 32, 21, 0]
# [54, 10, 43, 32, 21, 0, 'added']

Numbers.insert(3, 99)
# It addes the given data at the given position in the List
# [54, 10, 43, 32, 21, 0]
# [54, 10, 43, 99, 32, 21, 0]

Numbers.pop(2)
# It clears the data from the given index/ position from the List 
# [54, 10, 43, 32, 21, 0]
# [54, 10, 32, 21, 0] 

Numbers.remove(43)
# It clears the given data from the List 
