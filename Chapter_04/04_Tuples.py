# A tuple is a immutale(Can't change) Data type in python .
# A tuple is a collection which is ordered and unchangeable.
# We can assign a tuple using ()


t = (1, 2, 3, 4, 5)

# we can print the created tuple 
print (t)

# we can print the elements of the tuple
print (t[0])

# WE CAN NOT UPDATE THE VALUES OF A TUPLE 
# t[0] = 6 It throws an error 

# t1 = () # It's a Empty Tuple 

# t3 = (1) # Wrong way to declare a Tuple with single element  


t2 = (1,) # It's a Tuple with single element  
#  or we can assign like below
#  
# my_tuple = tuple(("any",)) it will print any as a single tuple 
# my_tuple = tuple("any",) but it will print a tuple with single single words 

my_tuple = tuple(("any",))
print(type(my_tuple))
print(my_tuple)


tuple_test = (True, "4", 4, 5.0)
print(tuple_test)

my_tuple1 = tuple(("apple",)) # If wer won't ass "," after a single tuple , as the string is iltrable so it will creat a tuple with the single single word of the string 
print(my_tuple1)

my_tuple += my_tuple1
print(my_tuple)

# as we created a tuple and assign some values to it , that is called as "packing" a tuple 
# but we can unpack the tuple as well  and the example is given below 

fruits = ("apple", "banana", "cherry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


another_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green1, yellow1, *red1) = another_fruits
# if there is a lot of values to unpack we can use *(asterisk) before the last variable to print all the rest unpacked values to the last variable as a list
print(green1)
print(yellow1)
print(red1)
