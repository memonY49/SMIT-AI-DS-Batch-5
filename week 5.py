"""
Multi dim list: list of lists.

data = [[1,2,4],
        [5,6,8],
        [9,6,5]]

for row in data:
    for column in row:
        print(column,end = " ")
    print()

"""






"""
userdata = [["Yasir","Nawaz","03000300000","abc@gmail.com","abc123"],
            ["Yasir1","Nawaz","03000300000","abc1@gmail.com","abc123"],
            ["Yasir2","Nawaz","03000300000","abc2@gmail.com","abc123"],
            ["Yasir3","Nawaz","03000300000","abc3@gmail.com","abc123"],
            ["Yasir4","Nawaz","03000300000","abc4@gmail.com","abc123"]]

useremail = input("Enter your email: ")
userpass = input("Enter your password: ")

for user in userdata:
    if user[3] == useremail and user[4] == userpass:
        print("Name:",user[0])
        print("Fname:",user[1])
        print("Phone:",user[2])
        print("Email:",user[3])
        break
else:
    print("User not found!")

"""
"""
create a multi dim list to store details for atleast 5 users.
create two more variables useremail and userpass and take input from the user.
match useremail and userpass with all the users if matched print all details of
that user only.
"""


"""
Task:
step1: create a multi dim list to store details of 3 cars for three companies.
step2: Show user a menu for choosing any of the company name.
step3: when user selects a company show a new menu for all available cars of
that company.
step4: when user selects any car print all details of that car.

data = [[["Toyota","Corola","GLI","2007",900000],
         ["Toyota","Corola","GLI","2007",900000],
         ["Toyota","Corola","GLI","2007",900000]],
        [["Suzuki","mehran","vx","2010",1000000],
         ["Suzuki","mehran","vx","2010",1000000],
         ["Suzuki","mehran","vx","2010",1000000]],
        [["kia","sportage","alpha","2020",5000000],
         ["kia","sportage","alpha","2020",5000000],
         ["kia","sportage","alpha","2020",5000000]]]


Required Output:
Menu 1:
    1. Toyota
    2. Suzuki
    3. Kia
Enter your selection: 1

Menu 2:
    1. Corola 1
    2. Corola 2
    3. Corola 3
Enter your selection: 2
        


data = [[["Toyota","Corola1","GLI","2007",900000],
         ["Toyota","Corola2","GLI","2007",900000],
         ["Toyota","Corola3","GLI","2007",900000]],
        [["Suzuki","mehran1","vx","2010",1000000],
         ["Suzuki","mehran2","vx","2010",1000000],
         ["Suzuki","mehran3","vx","2010",1000000]],
        [["kia","sportage1","alpha","2020",5000000],
         ["kia","sportage2","alpha","2020",5000000],
         ["kia","sportage3","alpha","2020",5000000]]]

#company = [company[0][0] for company in data]

for index, company in enumerate(data):
    print(index+1, company[0][0])
co = int(input("Enter your selection: "))
if co < len(data):
    print("*"*20)

    for index, car in enumerate(data[co-1]):
        print(index+1, car[1])
    ca = int(input("Enter your selection: "))
    if ca < len(data[co-1]):
        print("*"*20)

        print("Name:",data[co-1][ca-1][1])
        print("Model:",data[co-1][ca-1][2])
        print("Year:",data[co-1][ca-1][3])
        print("price:",data[co-1][ca-1][4])
    else:
        print("Wrong Selection...")
else:
    print("Wrong Selection...")
"""  
#mylist = [3,6,8,9,0]
#for i in mylist:
#    print(i)






















