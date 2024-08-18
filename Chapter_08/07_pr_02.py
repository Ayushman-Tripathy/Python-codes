def  celsius_to_fahrenheit(celsius):
   fahrenheit = (32 + (celsius * 1.8))
   return fahrenheit

celsius = int(input("Enter tempratuire in celsius: "))
c = celsius_to_fahrenheit(celsius)
print(f"Your temprature({celsius}) in fahrenheit is: {c}")
