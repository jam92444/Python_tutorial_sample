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
   

def fullName(fname,lname):
    print(f"{fname} {lname}")
    
fullName(lname="amri",fname="bushra")


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

'''

def addition(a):
    sum = 0 
    for i in a:
        sum += i;
    print(sum);
    

t1 = (1,2,3,4,5,6,7,8,9);
addition(t1)