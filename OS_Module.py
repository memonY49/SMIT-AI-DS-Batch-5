import os
import pathlib

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

# if os.path.exists("Data/A/test0.txt"):
#     os.remove("Data/A/test0.txt")
#     print("File removed!!")
# else:
#     print("file does not exists")


# try:
#     os.remove("Data/A/test0.txt")
#     print("File removed!!")
# except FileNotFoundError:
#     print("File not found")


# dir = "D:\\"
# folder = "salani"
# subfolder = "Batch 5"
# file = "data.txt"
# print(f"{dir}{folder}/{subfolder}/{file}")
# filepath = os.path.join(dir,folder,subfolder,file)
# print(os.path.split(filepath))
# print(os.path.splitext("filehandling.py"))
# print(os.listdir())

# listofdir = os.listdir()
# listofpy = []
# for file in listofdir:
#     exten = os.path.splitext(file)[1]
#     if exten == ".py":
#         listofpy.append(file)


# print(listofpy)


# path = "D:\\salani\\Batch 5\\Data\\B"
# print(os.path.dirname(path))


path =pathlib.Path("D:\\salani\\Batch 5\\Data\\B\\test1.txt")

# print(path.home())
# print(path.is_file())
# print(path.suffix)
# print(path.name)
file = path.open()
print(file.read())
file.close()
