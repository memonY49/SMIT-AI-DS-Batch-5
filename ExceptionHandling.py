# # Exception handling: to handle all user errors/runtime errors
# # -> In EH we have two cluases 1.try, 2.except
# # try: in try cluase we can use a block of code in which there can be an error in runtime.
# # except: except cluase executes when there is an error in try cluase.
# # sytax:
# #   try:
# #       body of try
# #   except:
# #       body of except

# # try:
# #     x = int(input("Enter a number: "))
# #     fle  = open("yasir.txt","r")
# # # except ValueError:
# # #     print("Enter a number only")
# # # except FileNotFoundError:
# # #     print("File not found")
# # except Exception as e:
# #     print(e)


# # while True:
# #     x = int(input("Enter a number: "))
# #     if x == 0:
# #         break


# # Create a Atm system.
# # Create two variables account_title and account_balance.
# # Show user a menu for 1. View account balance, 2. Withdraw, 3. Deposit, 0. Exit

# account_title = "Yasir Nawaz"
# account_balance = 20000000


# while True:
#     print(f"Wellcome {account_title}")

#     print("1. View Balnce\n2. Withdraw\n3. Deposit\n0. Exit")
#     for i in range(3):
#         try:
#             selection = int(input("Enter your selection: "))
#             break
#         except:
#             print(f"Error {i+1}: Enter a number only!!!")
#     else:
#         break
#     try:
#         if selection == 0:
#             break
#         elif selection == 1:
#             print(f"Current Balnce of your acount is: {account_balance}")
#         elif selection == 2:
#             amount = int(input("Enter your Amount: "))
#             if amount <= account_balance and amount%500 == 0 and amount>0:
#                 account_balance -= amount
#             else:
#                 print("Incorrect amount!!!")
#         elif selection == 3:
#             amount = int(input("Enter your Amount: "))
#             account_balance += amount
#         else:
#             print("Wrong selection!!!")
#     except:
#         print("Invalid Input !!!")



# # Create a Atm system.
# # Create a data.csv file add atleast 10 bank account details (account_title, balance, account_number, pin_code).
# # Show user a menu for 1. View account balance, 2. Withdraw, 3. Deposit, 0. Exit
# # Add login functionality with accountnumber and pin_code







x:int = int(input("Enter a number: "))
y:int = 8

if (x<y and x>5):
    print(f"{x} is less than {y}")
else: 
    print(f"{x} is not less than {y}")

