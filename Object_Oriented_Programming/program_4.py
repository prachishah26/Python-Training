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



# code is not completed yet-----------------------------------------------------------

l = []
class users:
    no_of_users = 0
    def __init__(self, username, account_no, mobile_no, address):
        self.username = username
        self.account_no = account_no
        self.mobile_no = mobile_no
        self.address = address
        self.account_balance = 5000
        users.no_of_users += 1



# a = input("enter name")
# b = input("enter account_num")
# c = input("enter mobile num")
# d = input("enter address")
# user = users(a,b,c,d)
# user = users(a,b,c,d)
# # l.append(user)

# print(user.username)


arr = []


class user_manager:

    def add_user(self):
        username = input("enter name")
        account_no = input("enter account no.")
        mobile_no = input("enter mobile no")
        address = input("enter address")
        
        user = users(username, account_no, mobile_no, address )
        arr.append("name : " + user.username + " , " + "account no. : " +  user.account_no)

    def get_existing_user(self):
        for user1 in range(len(arr)):
            print(arr[user1])

    def remove_user():
        pass

        
# test2 = user_manager()
# test2.add_user()
# test2.add_user()

# test2.get_existing_user()
# class ATM:
#     ac = input("enter your account number")
#     if ac not in user1.account_no:
#         print("enter valid account number")

# test = ATM()
