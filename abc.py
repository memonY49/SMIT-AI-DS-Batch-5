# for counter in range(1,11):
#     print(counter)

# counter = 1
# while(counter<=10):
#     print(counter)
#     counter += 1


try:
    int(input())
except FileNotFoundError:
    print("Error")
except ValueError:
    print("Enter Number only")