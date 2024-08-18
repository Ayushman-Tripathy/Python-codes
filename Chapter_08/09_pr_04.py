num = int(input("Enter a number: "))

def cal_of_first_n_natural_number(num):
        if num == 0:
            return 0
        else:
            sum = num + cal_of_first_n_natural_number(num-1)
            return sum 

p = cal_of_first_n_natural_number(num) 
print(f"The sum of the first {num} natural number is: {p} ")


# def cal_of_first_n_natural_number(n):
#     num = 0
#     for i in range(n+1):
#         num = num + i
#     return num

# n = int(input("Enter a number: "))
# sum = cal_of_first_n_natural_number(n) 
# print(f"The sum of the first {n} natural number is: {sum} ")
