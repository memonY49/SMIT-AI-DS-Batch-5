from datetime import datetime
import logging
# def greet():
#     print("Hello! And Wellcome")

#     def print_name():
#         print("My name is Yasir.")

#     print_name()
# greet()

error_logger = logging.getLogger("error")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('error.log')
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s"))
error_logger.addHandler(error_handler)

activity_logger = logging.getLogger("activity")
activity_logger.setLevel(logging.INFO)
activity_handler = logging.FileHandler('activity.log')
activity_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"))
activity_logger.addHandler(activity_handler)






def greet(func):
    def wrapper(*args, **kwargs):
        print("Hello! And Wellcome.")
        func(*args, **kwargs)
        print("GoodBye!!!")
    return wrapper

@greet
def print_name(name):
    print(f"My name is {name}")

# @greet
# def print_ahmed():
#     print("My name is ahmed")

# print_name("Yasir")
# print_ahmed()

#create a console based atm application:
#Show a menu to the user first where it says 
#1.view balance
#2.withdraw
#3.deposit
#0.exit
#show confirmation after every transection
#press y to confirm or n to decline.

def confirmation(func):
    def wrapper(*args, **kwargs):
        userin = input("Press y to confirm or n to decline")
        if userin.lower() == 'y':
            return func(*args,**kwargs)
        else:
            print("Your transection has been declined....")
    return wrapper

def thankyou(func):
    def wrapper(*args, **kwargs):
        print("Hello, Wellcome to my ATM")
        out = func(*args, **kwargs)
        print("Thank you for using this ATM.")
        return out
    return wrapper


def error_log(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            error_logger.exception(e)
            raise e
    return wrapper

def activity_log(func):
    def wrapper(*args,**kwargs):
        # with open("activity_log.txt","a") as file:
        #     file.write(F"{datetime.now()} function called: {func.__name__}\n")
        activity_logger.info(f"Function Called: {func.__name__}")


        return func(*args,**kwargs)
    return wrapper




def menu():
    print("1.View Balance\n2.Withdraw\n3.Deposit\n0.Exit")




@thankyou
@confirmation
@error_log
@activity_log
def viewBalance():
    print(f"Balance is: {balance}")


@thankyou
@confirmation
@error_log
@activity_log
def withdraw(balance):
    amount = int(input("Enter ammount for withdraw: "))
    return balance - amount

@thankyou
@confirmation
@error_log
@activity_log
def deposit(balance):
    amount = int(input("Enter ammount for withdraw: "))
    return balance + amount

balance = 10000

while(True):
    menu()
    choice = int(input("Enter your seleton: "))
    title = "Yasir Nawaz"
    

    if choice == 0:
        break
    elif choice == 1:
        viewBalance()
    elif choice == 2:
        balance = withdraw(balance)
    if choice == 3:
        balance = deposit(balance)



