# # 01. Test for 18+ or not 
age1 =int(input("Enter your Correct age: "))
if (age1>=18):
    print("Yes you are 18+")
else:
    print("Oops you are below 18")

# # 02. Your stage according to your age 
age = int(input("Enter your age: "))

if (age>=0 and age<=5):
    print("You are Baby ")

if (age>=6 and age<=14):
    print("You are Child ")

if (age>=15 and age<=21):
    print("You are Adolescence ")

if (age>=22 and age<=32):
    print("You are Youth ")

if (age>=33 and age<=45):
    print("You are Maturity ")

if (age>=46 and age<=64):
    print("You are Senior ")

if (age>=65):
    print("You are Old_age ")
