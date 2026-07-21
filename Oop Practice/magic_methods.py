# class student:
#     def __init__(self,name:str,id:str,cl:str):
#         self.name = name
#         self.id = id
#         self.cl = cl


# class studentManagment:
#     def __init__(self,name,school_id):
#         self.school_name = name
#         self.school_id = school_id
#         self.list_students = []

#     def add_student(self,std):
#         self.list_students.append(std)
    
#     def __len__(self):
#         return len(self.list_students)
    
#     def __str__(self):
#         return self.school_name
    
#     def __repr__(self):
#         return self.school_name

#     def __int__(self):
#         return self.school_id

#     def __add__(self, other):
#         self.add_student(other)
    
    
    
    
# school = studentManagment('SMIT',1)

# school.add_student(student("Yasir","std1","AIDS"))
# school.add_student(student("Yasir1","std1","AIDS"))
# school.add_student(student("Yasir2","std1","AIDS"))
# school.add_student(student("Yasir3","std1","AIDS"))

# # print(len(school))
# # print(school)
# # print(int(school))

# school + student("Ahmed","std2","AIDS")

# print(len(school))




class ATM:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
    def __str__(self):
        return f"Title: {self.title}\nBalance: {self.balance}"
    def __repr__(self):
        return f"Title: {self.title}\nBalance: {self.balance}"
    def __sub__(self, other):
        self.balance -= other
    def __add__(self, other):
        self.balance += other

    def __iadd__(self, other):
        self.balance += other
        return self
    
    def __isub__(self, other):
        self.__sub__(other)
        return self

    def __gt__(self, other):
        return self.balance > other.balance
    def __lt__(self, other):
        return self.balance < other.balance
    
    
    

myatm = ATM("Yasir",20000000000)
wifeAtm = ATM("Someone",100000000)
# myatm - 50000
# print(myatm)
# myatm + 100000
# print(myatm)

# myatm += 500000
# print(myatm)

print(myatm > wifeAtm)

print(myatm.__class__())
