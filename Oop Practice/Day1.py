# class human:
#     skin_color = None
#     legs = 2
#     ears = 2
#     eyes = 2
#     name = None
#     gender = None
#     def speak(self):
#         print("..............")
#     def run(self):
#         print("Human is runnig...")
#     def jump(self):
#         print("Human is jumping.....")

# # cunstructor method: It is used to create an object of a class.
# # -> this method is called by the name of the class.

# obj = human()
# obj1 = human()
# obj2 = human()

# print(obj.legs)
# obj.name = "Yasir"
# print(obj.name)
# print(obj1.name)

# obj.jump()


# scope of variables and methods:
#       1.object level: Which can only be called from an object
#               -> can only be called with object name
#       2.static:       which are same for all objects
#               -> can be called by itself or by class name


# class human:
#     eye = 2             # static variable
#     def __init__(self):
#         self.name = 'gjgkjhh'   # object level variable
#     def run():      # static method
#         print("running....!!!")        
#     def jump(self): # object level
#         print("jumping.....!!!!")

    

# human.eye = 3
# obj1 = human()

# # print(obj1.name)


# human.run()
# # human.jump(obj1)
# obj1.jump()





class student:
    def __init__(self,name:str,id:str,cl:str):
        self.name = name
        self.id = id
        self.cl = cl


class studentManagment:
    def __init__(self):
        self.list_students = []
    def add_student(self):
        name = input("Enter the name: ")
        id = input("Enter the id: ")
        cl  = input("Enter the class: ")
        std = student(name,id,cl)
        self.list_students.append(std)
        print("-----Student added------")
    def view_all_students(self):
        if len(self.list_students) == 0:
            print("No student found")
            return
        for std in self.list_students:
            print(std.name,std.id,std.cl)
            print("*"*20)
        

# std1 = student("Yasir","std1","AIDS")
# std2 = student("Yasir1","std2","AIDS")
# std3 = student("Yasir2","std3","AIDS")
# std4 = student("Yasir3","std4","AIDS")
# std1.name = "yasir"
# std1.id = 'std1'

my_school = studentManagment()
# my_school.add_student()
# my_school.add_student()
# my_school.add_student()
# my_school.add_student()

# my_school.view_all_students()
while True:
    print("1. Add Student\n2.view all students\n0. exit")
    choice = int(input("Enter your selection: "))
    if choice == 1:
        my_school.add_student()
    elif choice == 2:
        my_school.view_all_students()
    elif choice == 0:
        break










