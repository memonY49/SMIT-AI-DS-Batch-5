"""
dict: the collection of key and value pairs.
syntax:
    name_of_the_variable = {key:value}
to use:
    name_of_the_variable[key]
"""

mydict = {"name":"Yasir",
          "fname":"Nawaz",
          "phone":"030000000",
          "age":27,
          "email":"abc@gmail.com",
          "password":"abc123"}

#useremail = input("Enter your email: ")
#userpass = input("Enter your password: ")

#if match print all detail else "email or pass is wrong"

#if userpass == mydict["password"] and useremail == mydict["email"]:
#    print(mydict)
#else:
#    print("Email or password is wrong...!!")

#methods of a dict:

mydict = {"name":"Yasir",
          "fname":"Nawaz",
          "phone":"030000000",
          "age":27,
          "email":"abc@gmail.com",
          "password":"abc123"}
mydict["add"] = "jhdcjhasvcghsvcjasdghc"
mydict["age"] = 20

#print(mydict)

#keys()   : returns list of all keys of the dict
#values() : returns list of all values from the dict
#items()  : return list of tuple pair of key and value.

#print(list(mydict.keys())[0])
#print(mydict.items())

#for k,v in mydict.items():
#    print(k+":",v)


#print(len(mydict))
"""
data = {"std1":{"name":"Yasir1",
                "fname":"Nawaz",
                "phone":"030000000",
                "age":27,
                "email":"abc1@gmail.com",
                "password":"abc123"},
        "std2":{"name":"Yasir2",
                "fname":"Nawaz",
                "phone":"030000000",
                "age":27,
                "email":"abc2@gmail.com",
                "password":"abc123"},
        "std3":{"name":"Yasir3",
                "fname":"Nawaz",
                "phone":"030000000",
                "age":27,
                "email":"abc3@gmail.com",
                "password":"abc123"}}
"""
data_json = [{"name":"Yasir1",
                "fname":"Nawaz",
                "phone":"030000000",
                "age":27,
                "email":"abc1@gmail.com",
                "password":"abc123"},
             {"name":"Yasir2",
                "fname":"Nawaz",
                "phone":"030000000",
                "age":27,
                "email":"abc2@gmail.com",
                "password":"abc123"},
             {"name":"Yasir3",
                "fname":"Nawaz",
                "phone":"030000000",
                "age":27,
                "email":"abc3@gmail.com",
                "password":"abc123"}]


#print(data["std2"]["name"])

useremail = input("Enter your email: ")
userpass = input("Enter your password: ")


for user in data_json:
    if useremail == user["email"] and userpass == user["password"]:
        print(user)


















