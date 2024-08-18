factorial_value = int(input("Enter the factorial value: "))
original_number = 1
current_factorial = 1

while current_factorial < factorial_value:
    original_number += 1
    current_factorial *= original_number

if current_factorial == factorial_value:
    print(f"The original number is: {original_number}")
else:
    print("No original number found for the given factorial value.")
