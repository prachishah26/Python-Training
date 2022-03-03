# Create a class for Users,
# username
# account no
# mobile no
# address
# account balance
# -> Create a class for user manager
# Manages user => Add new user, Get existing user, remove user
# -> Create a class for ATM,
# Enter account no and get user if not found then show a valid message
# Show options for user operations like creating new users, View Balance. Deposit, Withdraw, Close account, etc...
# Transaction charge: 0.5 for every operation
# Account balance limit: 10000

class users:
    account_number_starts = 900001
    def __init__(self, username, mobile_no, address,account_balance):
        self.username = username
        self.account_no = users.account_number_starts
        self.mobile_no = mobile_no
        self.address = address
        self.account_balance = account_balance
        users.account_number_starts += 1

class user_manager:
    def __init__(self):
        self.total_users = []

    def add_user(self):
        pass

    def get_existing_user(self):
        if len(self.total_users) != 0:
            for user1 in self.total_users:
                print(f"account number : {user1.account_no}, Name of user : {user1.username}, balnce : {user1.account_balance}")
        else:
            print("\nUsers list is not available ")

    def remove_user(self, account_num):
        for user in self.total_users:
            if user[1].account_no == account_num:
                self.total_users.remove(user)

class ATM():
    def verifying_account(total_users, account_num):
        for user in total_users:
            if user.account_no == account_num:
                return user 
        return False

manager = user_manager()

while True:
    try :
        print("\nEnter 1 : to create new account")
        print("Enter 2 : functionalities for existing users")
        print("Enter 3 : To see existing users")
        print("Enter 4 : Quit")
        

        key_pressed = int(input("enter the operation number you want to do : "))

        if key_pressed == 1:
            username = input("\nEnter your name : ")
            mobile_no = input("enter your mobile number : ")
            address = input("Enter your address : ")
            
            while True:
                account_balance = int(input("Enter the amount you want to add : "))
                if account_balance < 10000:
                    print("You have to add minimum 10000 rupees while creating a new account. ")
                else : 
                    break
            user = users(username,mobile_no,address,account_balance)
            manager.total_users.append(user)
            print("\nYour account created successfully !!!")

        elif key_pressed == 2:
            while True: 
                print("\nenter 1 for view balance")
                print("enter 2 for Deposite")
                print("Enter 3 for withdraw ")
                print("Enter 4 for close the account")
                print("enter 5 for quit")
                second_key_pressed = int(input("\nEnter operation number you want to perform : "))

                if second_key_pressed == 1:
                    account_number = int(input("\nenter your account number"))
                    get_user = ATM.verifying_account(manager.total_users,account_number)
                    if get_user:
                        
                        print("Your account balance is ",get_user.account_balance)
                    else:
                        print("Account doesn't existed.")

                elif second_key_pressed == 2:
                    account_number = int(input("\nenter your account number"))
                    print("Enter the amount you want to deposite : ")
                    deposited_amount = int(input("enter here : "))
                    get_user = ATM.verifying_account(manager.total_users,account_number)
                    get_user.account_balance += deposited_amount

                elif second_key_pressed == 3:
                    account_number = int(input("\nenter your account number : "))
                    print("Enter the amount you want to withdraw")
                    
                    get_user = ATM.verifying_account(manager.total_users,account_number)
                    while True:
                        withdraw_amount = int(input("enter here : "))
                        if get_user.account_balance - withdraw_amount < (-0.5) : 
                            print("You don't have sufficient amount in your account")
                            
                        else :
                            break
                    get_user.account_balance -= withdraw_amount + 0.5

                elif second_key_pressed == 4:
                    print("You are going to close your account")
                    account_number = int(input("\nEnter your account nmber : "))
                    get_user = ATM.verifying_account(manager.total_users,account_number)
                    manager.total_users.remove(get_user)

                elif second_key_pressed == 5:
                    break
        elif key_pressed == 3:
            manager.get_existing_user()        
        elif key_pressed == 4:
            print("\nLooking forward to serve you again")
            break
    except :
        print("Please enter a valid number !!! ")

