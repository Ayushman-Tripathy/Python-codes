# f1 = input("Enter The Fruit Number 1: ")
# f2 = input("Enter The Fruit Number 2: ")
# f3 = input("Enter The Fruit Number 3: ")
# f4 = input("Enter The Fruit Number 4: ")
# f5 = input("Enter The Fruit Number 5: ")
# f6 = input("Enter The Fruit Number 6: ")
# f7 = input("Enter The Fruit Number 7: ")

# MyFruitList = [f1, f2, f3, f4, f5, f6, f7]
# print (MyFruitList)
# print ("Thanks :D")


mylist = []

while True:
    a= input(f"Enter any fruit name:\nPress enter to exit ")
    if a == "":
        break
    else:
        mylist.append(a)
print(mylist) 

