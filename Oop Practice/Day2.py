# class A:
#     x = 3
#     y = 7
#     def foo(self):
#         print("Foooooo.....")

# class B(A):
#     pass



# class Animal:
#     def __init__(self):
#         self.legs = None
#         self.eye = 2
#         self.color = None
#         self.tail = None
#         self.wings = None
#     def sound(self):
#         print("--------------")

# class cat(Animal):
#     def __init__(self):
#         self.tail = True
#         self.wings = False
#         self.legs = 4
#     def sound(self):
#         print("Meow.......")


# cat1 = cat()
# cat1.sound()
# print(cat1.tail)

# ani1 = Animal()
# print(ani1.wings)



class Animal:
    def __init__(self,legs,eye,color= None):
        self.legs = legs
        self.eye = eye
        self.color = color
        

class Human(Animal):
    def __init__(self, name:str, age:int, height:int, **kwargs):
        self.name = name
        self.age = age
        self.height = height
        super().__init__(**kwargs)

class student(Human):
    def __init__(self,id:str,cl:str,**kwargs):
        self.id = id
        self.cl = cl
        super().__init__(**kwargs)
    def getid(self):
        return self.id
    def getcl(self):
        return self.cl
    
    def setid(self,id):
        self.id = id
    def setcl(self,cl):
        self.cl = cl
    


std1 = student('std1','AIds',name= "Yasir", age=27, height = 160, legs = 2, eye = 2, color = 'Brown')


std1.setcl('DM')
print(std1.getcl())