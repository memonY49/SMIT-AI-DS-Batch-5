class human:
    skin_color = None
    legs = 2
    ears = 2
    eyes = 2
    name = None
    gender = None
    def speak(self):
        print("..............")
    def run(self):
        print("Human is runnig...")
    def jump(self):
        print("Human is jumping.....")

# cunstructor method: It is used to create an object of a class.
# -> this method is called by the name of the class.

obj = human()
obj1 = human()
obj2 = human()

print(obj.legs)
obj.name = "Yasir"
print(obj.name)
print(obj1.name)

obj.jump()