def inch_to_centimeter(inch):
    centimeter = inch * 2.54
    return centimeter


num = int(input("Enter the length in Inches: "))
p = inch_to_centimeter(num)
print(f"Your length in centimeters is {p}")