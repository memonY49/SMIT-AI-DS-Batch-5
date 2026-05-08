"""
    Conditional statements:
        syntax:
            if condition :
                body of if
            else:
                body of else
        -> else can only be used with an above if 


x = 4
y = 6

if x<y:
    print("less than")
if x>y:
    print("greater than")
else:
    print("equals")
"""


# create a variable named as age
# store some age in that variable
# if age < 15 the person is in school.
# compare if age>15 and <25 the person is called collage passed.
# if age>25 and < 30 the person is uni passed
# if age> 30 the person is in masters.
"""

age = 30
if age<15:
    print("the person is in school")
if age>=15 and age<25:
    print("the person is called collage passed.")
if age>=25 and age<30:
    print("the person is uni passed")
if age>=30:
    print("the person is in masters.")
"""

# Task 1:
# step 1: Create at least 5 variable(name,fname,phone,email and password)
# step 2: Create two extra variables for useremail and userpass take as an input
# from the user
# step 3: Match email == useremail and password == userpass
# step 4: If matched print all details else "email or password was incorrect"
"""
name = "yasir"
fname = "nawaz"
phone = "0300000000"
email = "abc@gmail.com"
password = "abc123"

useremail = input("Enter your email: ")
userpass = input("Enter your password: ")

if email == useremail and password == userpass:
    print(name)
    print(fname)
    print(phone)
    print(email)
else:
    print("email or password was incorrect")
"""


"""
x = 5
y = 6

if x < y:
    print("less than")
elif x > y:
    print("greater than")
else:
    print("equals than")
"""



# Nasted if:
#       if inside of an if
"""
x = 6
y = 8

if x<y:
    if x>0:
        print("x is in range of 0 - 8")
"""

"""
name = "yasir"
fname = "nawaz"
phone = "0300000000"
email = "abc@gmail.com"
password = "abc123"

useremail = input("Enter your email: ")
userpass = input("Enter your password: ")

if email == useremail:
    if password == userpass:
        print(name)
        print(fname)
        print(phone)
        print(email)
    else:
        print("password is incorrect")
else:
    print("email is incorrect")
"""


#task :
# take number variable from the user and check if the number is even than
# print "even number" else print "odd number"


number = int(input("Enter your number: "))
if number%2 == 0:
    print("number is even")
else:
    print("number is odd")




































