import os

# print(os.environ['yasir'])
# print(os.environ['PATH'])

# print(os.getcwd())
# os.chdir("D:\\")

# print(os.getcwd())

# print(os.listdir('D:\\salani'))

# os.mkdir("Data/B/F.txt")

# datadir = list(os.walk("Data"))

# for path, folders, files in datadir:
#     print(f"{path}")
#     print(f"Folders {len(folders)}: {folders}")
#     print(f"Files {len(files)}: {files}")
#     print("*"*10)



# os.system("rmdir data")

if os.path.exists("Data/A/test0.txt"):
    os.remove("Data/A/test0.txt")
    print("File removed!!")
else:
    print("file does not exists")


