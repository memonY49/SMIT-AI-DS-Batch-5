from collections import *

# Fuctions: A block of code seperated to perform a special task
# syntax:
#       def function_name( Parameters ):
#           body of a funcion.
# 
# Type of functions:
#   1. function with no parameter or any returning value.
#   2. function with some parameter and no any returning value.
#   3. function with no parameter but having a returning value.
#   4. function with some parameter and a returning value.



# def add(a,b):
#     print(a+b)

# def sub(a,b):
#     print(a-b)

# def mul(a,b):
#     print(a*b)

# def div(a,b):
#     print(a/b)



# x = int(input())
# y = int(input())

# choice = int(input("1.add\n2.sub\n3.mul\n4.div"))
# if choice == 1:
#     add(x,y)
# elif choice == 2:
#     sub(x,y)
# elif choice == 3:
#     mul(x,y)
# elif choice == 4:
#     div(x,y)



# def add():
#     x = int(input("Enter your no: "))
#     y = int(input("Enter your no: "))
#     return x+y

# result = add()
# print(result)


# Task1: Take a String as an input from user to check.
#       Create a func that takes string as an argument and return if string is palindrome returns True else False

# Task2: Create a function to find nth number of fibonacci



def find_fibonaci(n):
    if n<0:
        return None
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a+b
        return a
#     a = 0
#     b = 1
#     if n<0:
#         return None
#     elif n == 1:
#         return a
#     elif n == 2:
#         return b
#     else:
#         for _ in range(n-2):
#             c = a+b
#             a = b
#             b = c
#         return c
  
# print(find_fibonaci(int(input())))


# task 3: create a function to count words in a string and return a dictionary.

# string: "Im learning Python from python with yasir."
# return: {"im":1,"learning":1,"python":2,"from":1,"with":1,"yasir.":1}

def word_counter(text):
    words = text.lower().split(' ')
    print(words)
    # results = {}
    # for w in words:
    #     if w not in results:
    #         results[w] = words.count(w)
    # return results
    return dict(Counter(words))


userinp = input("Enter a sentance to count: ")
print(word_counter(userinp))


# labels = ["Name","Fname","Email","Phone"]
# values = ["Yasir","Nawaz","abc@gmail.com","03444444444444"]
# result = {}

# for l, v in zip(labels,values):
#     result[l] = v

# print(result)





