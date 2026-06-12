# file = open("data.txt", "r")

# print(file.read()) # .read() is used to read complete file as a single string
# print(file.readline()) # .readline() is used to read one line at a time

# mystr = " "
# while mystr != "":
#     mystr = file.readline().replace("\n","")
#     print(mystr)

# print(file.readlines())

# for line in file.readlines():
#     print(line.strip())

# useremail = input("Enter your email:")
# userpass = input("Enter your password:")
# for user in file.readlines():
#     data = user.strip().split(",")
#     if useremail == data[3] and userpass == data[4]:
#         print(data)

# data = [user.strip().split(",") for user in file.readlines()]
# print(data)

# file.close()
# data = [["Yasir2","Nawaz","03000003000","abc2@gmail.com","abc123"],
#         ["Yasir3","Nawaz","03000003000","abc3@gmail.com","abc123"],
#         ["Yasir4","Nawaz","03000003000","abc4@gmail.com","abc123"],
#         ["Yasir5","Nawaz","03000003000","abc5@gmail.com","abc123"]]
# str_data  = [",".join(line)+"\n" for line in data]
# # print(str_data)
# # print(",".join(user))

# list_str = ["hjgjghvhs\n","jnkjbasjhfbvasdjh\n","ygutatasdf\n","hgfjvjhfgjsda\n"]

# with open("data.txt","w") as file:
#     # for user in data:
#     #     file.write(",".join(user)+"\n")
#     file.writelines(list_str)



# with open("data.txt","a") as file:
#     file.write("jkbjhbjhkghhvmsd\n")

# with open("data.txt","a+") as file:
#     file.seek(0)
#     print(file.read())
    
    # file.write("yasir nawaz")








# Create a user menu for add, view by id and view all students
# If user selects Add a student option get student details from that user include (id, 
# name,fname,phone,email and password)
# If user selects view by id than ask user for id if matched show all details of that student
# else print student not found
# If user selects view all students than show all details about all students.

userselection = int(input("1.Add student\n2.View by id\n3.View All\n4.delete by id\nplease select an option: "))

if userselection == 1:
    # S_ID = input("Enter ID of the Student: ")
    name = input("Enter Name of the Student: ")
    fname = input("Enter FName of the Student: ")
    email = input("Enter Email of the Student: ")
    password = input("Enter Password of the Student: ")
    with open("data.csv","a+") as file:
        file.seek(0)
        # If student id is manual
        # ids = [user.strip().split(',')[0] for user in file.readlines()]
        # if S_ID not in ids:
        #     file.write(f"{S_ID},{name},{fname},{email},{password}\n")
        # else:
        #     print("Student Id already registered!!")
        next_id = f"std-{len(file.readlines()) + 1}"
        file.write(f"{next_id},{name},{fname},{email},{password}\n")
    


elif userselection ==2:
    with open("data.csv","r") as file:
        userid = input("Enter Student ID:")
        for user in file.readlines():
            data = user.strip().split(",")
            if data[0]==userid:
                print(data)
        else:
            print("Student not found")

elif userselection == 3:
    with open("data.csv","r") as file:
        for user in file.readlines():
            data = user.strip().split(",")
            print(data)

elif userselection == 4:
    id_to_remove = input("Enter Student ID: ")
    data = []
    with open("data.csv","r") as file:
        for user in file.readlines():
            user = user.strip().split(',')
            if not user[0] == id_to_remove:
                data.append(user)
    str_data  = [",".join(line)+"\n" for line in data]
    with open("data.csv","w") as file:
        file.writelines(str_data) 

elif userselection == 5:
    id_to_update = input("Enter Student ID: ")
    data = []
    with open("data.csv","r") as file:
        for user in file.readlines():
            user = user.strip().split(',')
            if user[0] == id_to_update:
                user[1] = input("Enter Your Name to Update: ")
                user[2] = input("Enter Your FName to Update: ")
                user[3] = input("Enter Your Email to Update: ")
                user[4] = input("Enter Your Password to Update: ")
            data.append(user)
    str_data  = [",".join(line)+"\n" for line in data]
    with open("data.csv","w") as file:
        file.writelines(str_data) 

else:
    print("Wrong selection!!")