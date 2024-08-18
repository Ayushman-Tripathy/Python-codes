list = []

while True:
    user_input = input('Enter a number (or press Enter to quit): ')
    
    if user_input == "":
        break
    
    list.append(int(user_input))
1

list.sort()
print("Smallest number",list[0])
print("Greatest number",list[-1])