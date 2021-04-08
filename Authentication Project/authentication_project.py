#register
#- first name, last name, password, email
#- generate user id

#login
#- account number and password

#Bank Operations

#Initializing the system
import random

database = {} # dictionary

def init():
    
    print("Welcome to Python Bank")

    haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))
        
    if(haveAccount == 1):
        
        login()

    elif(haveAccount == 2):
        
        print(register())
    else:
        print("You have selected an invalid option")
        init()


def login():
    
    print("Login to you account")

    accountNumberFromUser = int(input("Enter your account number \n"))
    password = input("Enter your password \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               

    print("Invalid account number or password")
    login()

   

def register():
    
    print("***Register Now***")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has Been Created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()
    
def bankOperation(user):
    
    print("Welcome %s %s" % (user[0], user[1]))
    
    
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
               
        depositOperation()
    
    elif(selectedOption == 2):
        
        withdrawalOperation()
    
    elif(selectedOption == 3):
        
        login()

    elif(selectedOption == 4):
        
        exit()

    else:
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("Withdraw Cash")

def depositOperation():
    print("Deposit Cash")

def generateAccountNumber():

    return random.randrange(1111111111, 9999999999)

def logout():
    login()

#### Actual Banking System ####

init()

    

