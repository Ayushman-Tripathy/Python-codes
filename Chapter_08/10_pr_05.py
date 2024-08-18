def star_pattern(n):
    for i in range(n,0,-1):
        print("* " * i)

# def star_pattern(n):
#     for i in range(n):
#         print("* " * (n-i))
#     return

num = int(input('Enter a number: '))
star_pattern(num)
