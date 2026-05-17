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

#user = ["Yasir","Nawaz","03000300000","abc@gmail.com","abc123"]
#labels = ["Name","Fname","Phone","Email","Password"]

#for l,v in zip(labels,user):
#    print(l,v)


"""
mylist = [1,2,"a","b",2.4,5.6,True,False]

mylist[8] = 3.4

print(mylist[4])
"""

"""
Tuple: A collection of elements with any dtype where tuple is imutable.
syntax:
    variable_name_for_tuple = (elements seperated by coma)
"""

#mytuple = (1,2,3.4,5.5,"a","b",True)

#mytuple[3] = 4.9

#print(mytuple[3])

"""
Set: An unorder collection of non similer elements with any dtype.
syntax:
    variable_name_for_set = {elements seperated by coma}
"""

#myset = {1,2,3.5,4.6,1,True,False,'a','b',0}
#print(myset[2])

"""
How to use a method from any class:  objectoftheclass.nameofmethod()
List Methods:
    append( Element to add)	Adds an element at the end of the list
    clear()			Removes all the elements from the list
    copy()			Returns a copy of the list
    count(Element)		Returns the number of elements with the specified value
    extend()		        Add the elements of a list (or any iterable), to the end of the current list
    index(Element)		Returns the index of the first element with the specified value
    insert(Index, Element)	Adds an element at the specified position
    pop()			Removes the element from last of the ist
    remove(Element)		Removes the item with the specified value
    reverse()		        Reverses the order of the list
    sort()			Sorts the list
"""


#mylist = [3,9,5,8,9]
#mylist.append(10)
#mylist.insert(2,10)
#mylist.extend([10,11,15])

#print(mylist)
#removed = mylist.pop(2)
#mylist.remove(9)
#mylist.clear()
#mylist.reverse()
#mylist.sort(reverse = True)

#print(mylist)
#print(mylist.count(9))
#print(mylist.index(9))
#print()
#print(removed)


#element_count = mylist.count(9)
#for i in range(element_count):
#    mylist.remove(9)

#print(mylist)

set1 = {2,3,4,4,5,7,10}
set2 = {3,8,9,6,11,15}
print("set1:",set1)
print("set2:",set2)

#print(set1.union(set2))
#print(set1.intersection(set2))
#print(set2 - set1)
print(set1.union(set2) - set1.intersection(set2))
print(set1.symmetric_difference(set2))






    
