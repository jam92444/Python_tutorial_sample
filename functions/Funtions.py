''' 
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

'''
#Creating a Function
# to create we use 
# def funtion_name():
#   //block of code

# def addition(a,b):
#     print(a+b);
    
# def allmath(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a//b)
#     print(a**b)
    
# allmath(12,10)
    
''' 

Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def functionname(Arguments1,argument2):
    //statement or block of code
    

def familyname(middlename):
    print(f"Mohamed {middlename} Jamal");
    
familyname("Rashid");
familyname("Arif");
familyname("Rehan");
familyname("Imran")
familyname("Irfan")


Arbitrary Arguments, *args


If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

    

def addition(*a):
    sum = 0 
    for i in a:
        sum += i;
    print(sum);
    
addition(1,2,3,4,5)


# Keyword Arguments

You can also send arguments with the key = value syntax.
   
'''

# def fullName(fname,lname):
#     print(f"{fname} {lname}")
    
# fullName(lname="amri",fname="bushra")


'''

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

sas = {
    "fname":"Tobias",
    "lname":"Refsnes",
    "mname":"djkfsdkjfsj"
}

def my_function(**sas):
    
  print(sas['fname'])

my_function(fname = "Tobias", lname = "Refsnes",mname="djkfsdkjfsj")


def addition(a):
    sum = 0 
    for i in a:
        sum += i;
    print(sum);
    

t1 = (1,2,3,4,5,6,7,8,9);
addition(t1) 

# login
def login(username,password):
    userData = [
        {
            "username":"jamal",
            "password":"1231"
        },
        {
            "username":"falak",
            "password":"1231"
        },
        {
            "username":"arif",
            "password":"1231"
        },
        {
            "username":"bushra",
            "password":"1231"
        },
        {
            "username":"rehan",
            "password":"1231"
        },
    ]
    
    if((not username) or (not password)):
        print("Username and password required");
        
    found = False; #initial value
    
    for user in userData: #
        
        if(user['username']==username and user['password']==password): #False
            
            print(f"hey! {username} welcome back!"); #pass
            
            found = True 
            break;
        
    # found = false   
    if found==False:
        print(f"{username} not found")
    return;


    
username = input("Enter username: ");
password = input("Enter password: ");
login(username=username,password=password);

'''


#register form 
def register(username,email,password,phone):
    userData = [
        {
            "username":"Jamal",
            "email":"jamal1231@gmail.com",
            "password":"jamal@1121",
            "phone":"1234567891"
        },
        {
            "username":"yusuf",
            "email":"yusuf@gmail.com",
            "password":"yusuf@1121",
            "phone":"1234567891"
        },
        {
            "username":"rehan",
            "email":"rehan@gmail.com",
            "password":"rehan@1121",
            "phone":"1234567891"
        },
        {
            "username":"bushra",
            "email":"bushra@gmail.com",
            "password":"jamal@1121",
            "phone":"1234567891"
        },
    ];
    
    #checking if the values are empty
    if(not username or not password or not email):
        print("Username, Email and Password are required.")
        return
    
    found = False;
    
    #check the phone number is valid
    if phone:
        if len(phone)<10 or len(phone)>10:
            print("Enter a valid Phone Number");
            return;
    
    #check if email already exist
    for user in userData:
        if user['email'] == email:
            found = True
            break;
    if found:
        print(f'{email} already exist.');
        return;
    
    
    #checking if password is lessthan 8 char 
    if len(password) < 8:
        print("Password must be 8 or more than 8 character long");
        return;
    newUser = {
        "username":username,
        "password":password,
        "email":email,
        "phone":phone
    }
    userData.append(newUser);
    
    print("User registered Successfully");
    
    print(newUser)
    
    return;


username = input("Enter username: ");
email = input("Enter your email address: ");
password = input("Enter password: (must be 8 character long) ");
phone = input("Enter your Phone Number: ");

register(username,email,password,phone)

            
            
       
        
    
    

















