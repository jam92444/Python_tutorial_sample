# CONDITIONAL STATEMENT

# a = 12
# b = 13

'''
syntax
if (condition):

    //statement


# '''
# if a<b:
#     print("b is greater")
    
    
# username = input("Enter your username: ");
# email = input("Enter your email: ");
# password = input("Enter your password: ");

# # if (not username or not password or not email):
# #     print("Please enter all the fileds");
# # else:
# #     print("Welcome back!!")

# if (username and password and email):
#     print(f"Welcome {username}!!!")
# elif(not password):
#     print(f"please enter your password");
# elif(not email):
#     print(f"please enter your email");
# else:
#     print(f"please enter your username");
    
#nested if 

age = int(input("Enter age : "))
license1 = input("DO you have you driving license:(Y/N) ");

if age >= 18:
    if license1 == "Y" or license1 == "y":
        print("You are eligible for driving");
    else:
        print("You are not eligible or driving")
else:
    print("You are not eligible or driving")
    