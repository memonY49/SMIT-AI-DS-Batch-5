file = open("data.txt","r")

# print(file.read()) # .read() is used to read complete file as a single string
# print(file.readline()) # .readline() is used to read one line at a time

# mystr = " "
# while mystr != "":
#     mystr = file.readline()
#     print(mystr)

# print(file.readlines())

# for line in file.readlines():
#     print(line.strip())

for user in file.readlines():
    print(user.strip().split(",")[3])

file.close()