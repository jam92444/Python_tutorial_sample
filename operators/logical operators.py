#Logical operators 

#Types 
#1. And operator when both conditions are satisfied
# > greater than 
# < less than 
#logical gates.
# A   B   A and B
# T   T     T
# T   F     F
# F   T     F
# F   F     F
#AND T+T = True otherwise false 
# 10 less than 20 (true) && 20 greater than 10 (true)
# a = 10
# b = 20
# print(a<b and b>a)

# if(a>=10 and b <=20):
#     #if (a is greater than 10 or a is equal to 10) and (b is less than 20 or b is equal to 20) if true return print(a , b)
    
#     print(a , b)
# else:
#     print("Both conditions are false")

 
 
 
#2. Or operator any one conditions must satisfied

#logical gates.
# A   B   A or B
# T   T     True
# T   F     True
# F   T     True
# F   F     False
#or F+F = FALSE otherwise TRUE 

# a = 10
# b = 20
#     # F     F =true
# if(a>10 or b>21):    
#     print("one condition satisfied...")
# else:
#     print("Both conditions are false")



# not operator 

# logic table
# T  F
# F  T



# a =int(input("Enter Your Value: "));
# print(a!=18)
# if(a!=18):
#     print(f'{a} is not 18.');
# else:
#     print(f'{a} is 18.')
# username = input("Enter your name: \n");
# email = input("Enter your email: \n");
# password = input("Enter your Password: \n");

# if(not username or not email or not password):
#     print("Enter all fields");
# else:
#     print(f'Username : {username}')
#     print(f'email : {email}')
#     print(f'password : {password}')

# a = 10
# b = 20 
# c = 30
#     #  F and F =F
# # if not(a<b and b>a) and not((b>a and b<c) and (c>b and c>a)):
# #     print('c is greater')
# if(not a): #a = T but not F
#     print("A is empty");
# else:
#     print(f'A has value {a}')

# 123a = 12 #cannot include number before the char invalid
# a12 = "sdkfd" #number after char allowed
# a_u23 = "sample" #underscore allowed
# @hello = "12" # special char not allowed.add()
# a-sdjkf = 'hi'#using operator in a variable is not allowed .