# def factorial_itrative(n):
#     result = 1
#     for i in range(n):
#         result = result * (i+1)
#     return result

# f1 = factorial_itrative(5)
# print(f1)


def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n-1)

f2 = factorial_recursion(4)
print(f2)
