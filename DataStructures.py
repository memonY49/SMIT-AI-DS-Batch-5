# import collections
# from collections import *
import collections as cl

# Queue : These structure uses FIFO opeations (First in First Out)
# myque = cl.deque(["Banana","Mango","Orenge","Apple"])
# myque.append("dragonfruit")
# print(myque.popleft())

# print(myque)

# chainMap: 

# baseline = {'music': 'bach', 'art': 'rembrandt'}
# adjustments = {'art': 'van gogh', 'opera': 'carmen'}
# mychainmap = cl.ChainMap(adjustments, baseline)
# print(list(mychainmap.items()))

# user = {"Name":"Yasir","FName":"Nawaz","Email":"abc@gmail.com"}
# adjustment = {"Email":"yasir123@gmail.com","pass":"abc123"}
# data = cl.ChainMap(adjustment,user)
# data = data.new_child({"pass":"xyz123"})
# print(list(data.items()))

# counter

# mycounter = cl.Counter(["Banana","Mango","Orenge","Apple","Apple"])

# print(mycounter["dragonfruit"])

# UserDict

user = cl.UserDict({})

user.setdefault("email","abc@xyz.com")
user.setdefault("name","abc")
user.setdefault("fname","xyz")
# user['email'] = "abc@gmailcom"

print(user)