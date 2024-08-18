def greet(name="Stranger"): 
# The "Strager" is the default if a user will not  put correct argument 
# then Strager will enter as the argument
    return print('Good Day '+ name )

name = input("Enter your name: ")

greet()
# Stranger will pass
greet(name)
# USer input will pass
