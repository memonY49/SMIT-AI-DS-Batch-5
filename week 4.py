"""
List:
    A collection of elements with any dtype.
syntax for initializing a list:
    name_of_a_variable = [elements seperated by coma]
    
syntax for using a list:
    name_of_a_variable[index]
    

"""

#mylist = [1,2,"a","b",2.4,5.6,True,False]
#print(mylist[4])
"""
user = ["Yasir","Nawaz","03000300000","abc@gmail.com","abc123"]
labels = ["Name","Fname","Phone","Email","Password"]

useremail = input("Enter your Email: ")
userpass = input("Enter your Password: ")
if useremail == user[3] and userpass == user[4]:
    for i in range(0,4):
        print(labels[i],user[i])
else:
    print("Email or Password is wrong!!!")
"""

user = ["Yasir","Nawaz","03000300000","abc@gmail.com","abc123"]
labels = ["Name","Fname","Phone","Email","Password"]

for l,v in zip(labels,user):
    print(l,v)
















    
