num = int(input('Enter a number: '))

if num <= 0:
    print('Enter a valid positive number :(')

else:
    for i in range(10,0,-1):
        print(f'{num} * {i} = {num*i}')