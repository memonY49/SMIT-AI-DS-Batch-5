"""
dict: unorder the collection of key and value pairs.
syntax:
    name_of_the_variable = {key1:value1,key2:value2}
    
-> keys could not be same but you can use multiple dtypes.
-> we can use multiple dtypes in values.

to use:
    name_of_the_variable[key]
"""

mydict = {"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03000000",
          "age":27,
          "email":"abc@gmail.com",
          "password":"abc123"}

"""
print(mydict["name"])
mydict["age"] = 25
mydict["add"] = "bhsjbvshbvshkajvbasjhvbajhvbaskjhv"

print(mydict)

mydict2 = {0:"A",
           1:"B",
           2:"C"}

print(mydict2)
"""

#Dict Methods.
#keys()   : returns list of all keys of the dict
#values() : returns list of all values from the dict
#items()  : return list of tuple pair of key and value.
"""
print(list(mydict.keys()))
print(list(mydict.values()))
print(list(mydict.items()))
"""
#for k, v in mydict.items():
#    print(k+":",v)


data = {"std1":{"name":"Yasir1",
                "fname":"Nawaz",
                "phone":"03000000",
                "age":27,
                "email":"abc1@gmail.com",
                "password":"abc123"},
        "std2":{"name":"Yasir2",
                "fname":"Nawaz",
                "phone":"03000000",
                "age":27,
                "email":"abc2@gmail.com",
                "password":"abc123"},
        "std3":{"name":"Yasir3",
                "fname":"Nawaz",
                "phone":"03000000",
                "age":27,
                "email":"abc3@gmail.com",
                "password":"abc123"}}

#for sid,std in data.items():
#    print("std id:",sid)
#    for k,v in std.items():
#        print(k,":",v)
#    print("_"*20)


data = [{"name":"Yasir1",
         "fname":"Nawaz",
         "phone":"03000000",
         "age":27,
         "email":"abc1@gmail.com",
         "password":"abc123"},
        {"name":"Yasir2",
         "fname":"Nawaz",
         "phone":"03000000",
         "age":27,
         "email":"abc2@gmail.com",
         "password":"abc123"},
        {"name":"Yasir3",
         "fname":"Nawaz",
         "phone":"03000000",
         "age":27,
         "email":"abc3@gmail.com",
         "password":"abc123"},]

useremail = input("Enter your email: ")
userpass = input("Enter your pass: ")
for std in data:
    if std["email"] == useremail and std["password"] == userpass:
        #print(std)
        for k,v in std.items():
            print(k,":",v)
        break
else:
    print("user not found")

"""
std id: std1
name: Yasir1
fname: Nawaz
phone: 03000000
age: 27
email: abc@gmail.com
password: abc123
________________________
std id: std2
name: Yasir2
fname: Nawaz
phone: 03000000
age: 27
email: abc@gmail.com
password: abc123
________________________
std id: std3
name: Yasir3
fname: Nawaz
phone: 03000000
age: 27
email: abc@gmail.com
password: abc123


"""














