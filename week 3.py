

# Loops:
#   repeating a block of code for multiple times at same place until
#   the condition is true
#   types of loops:
#       1. for
#       2. while
#

# for loop:
#   syntax:
#       for counter in range(lb, ub):
#           body of loop


#for counter in range(1,11):
#    print(13,"X",counter,"=",counter*13)

# while loop:
#   syntax:
#       intialize counter
#       while(condition):
#           body of while
#           inc/dec

#counter = 10
#while counter >=1:
#    print(counter)
#    counter -= 1

"""
* * * *
* * * *
* * * *
* * * *
"""

#for i in range(1,5):
#    print("* "*4)

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

i = 1
while i<=5:
    print("* "*i)
    i+=1
    
j = 4
while j>=1:
    print("* "*j)
    j-=1


for i in range(1,6):
    print("* "*i)
for j in range(4,0,-1):
    print("* "*j)
"""


"""
print parameters:
    1. str|String|text : The string to be printed
    2. sep             : To seperate two or more strings
    3. end             : By default it ends the line and
                         starts a new line for next print
"""

#print("Hello",end=" ")
#print("world")

#print("Hello","World",sep = "_")


"""
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""

"""
for i in range(1,6):
    print("-"*(5-i),end="")
    print("* "*i)
    
for i in range(1,6):
    print("-"*i,end="")
    print("* "*(5-i))
"""
#task 1:
#   ask user about a number and print factorial of that number
"""
number = int(input("Enter Your Number: "))
fact = 1
for i in range(number,0,-1):
    fact = fact * i
print(fact)
"""

#task 2:
#   print a series of fibonacci " 0, 1, 1, 2, 3, 5, 8, 13, 21, 34"


a = 0
b = 1
print(a,b, end = ",",sep = ",")
for i in range(10):
    c = a+b
    print(c,end = ",")
    a = b
    b = c

























