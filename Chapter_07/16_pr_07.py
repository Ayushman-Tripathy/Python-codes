num = int(input('Enter a number: '))

for i in range(1,num+1):
    print(" " * num , end="")
    num = num-1
    print("*" * ((i*2)-1) , end ="")
    print(" " * num )