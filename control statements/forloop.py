'''
    FOR LOOP 
    
    >> With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
    
    
    
'''

''' 
    FOR IN LOOP 
    
    
    >> for in loop same as for loop 2 (value ,range)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


Looping Through a String

for x in "banana": # condition i=0 ;i < 6 which is the length of something called variable  ; i++;
  print(x)
  
  
  
The break,continue Statement  

fruits = ["apple", "banana", "cherry"]
for x in fruits: #true 
# apple ,banana
  if x == "banana": #f,t
    # print("hey iam conditional based statement: ",x)
    continue
  print(x) #apple
  
  
  
  
  
for x in range(6);

range instruction 

initial value = 0;
increment +1
value = 6 length

i=0, i<6 , i+=1


# def range(value):

#     for (i=0,i<length,i+1);
    
#         print(x)
        
# for x in range(2, 6): #(initial value ,length)
#   print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")




for x in range(6):
  if x == 5: 
    break
  print(x)
else:
  print("Finally finished!")
'''  

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj: 
    
#   for y in fruits: 
      
#     print(x, y) 
#     # first iteration red,apple ; red,banana ; red,cherry
#     # second iteration big,apple ; big,banana ; big,cherry
#     # third iteration tasty,apple ; tasty,banana ; tasty,cherry



# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
  

'''   
  
  x - value carry 
  
  i = i<length(vable)
  i = i< range
  
  range(number of iteration)
  
  

'''
  
# password = input("Enter your password: ");

# if(password):
#   if len(password)>=8:
#     print(f"your password {password}")
#   else:
#     while len(password)<8:
#       print("Enter password more than 8 char");
#       password = input("Enter your password: ");

#       if len(password) >=8:
#         print(f"Your password is {password}")
#         break;



# name = input("Enter your name : ")
# while (not name):
#   name = input("Enter your name : ")
#   if(name):
#     break;
# age = int(input("Enter your age : "))
# while (not age):
#   age = input("Enter your name : ")
#   if(age):
#     break;
# email = input("Enter your email : ")
# while (not email):
#   email = input("Enter your email : ")
#   if(email):
#     break;
# password = input("Enter your password : ")
# while (not password):
#   password = input("Enter your name : ")
#   if(password):
#     break;
  
# if(name and email and age and  password):
#   print(f"Name: {name}")
#   print(f"age: {age}")
#   print(f"email: {email}")


name = input("Enter your name : ")
email = input("Enter your enail : ")
age = int(input("Enter your age : "))

  
if (not name or not email and not age):
  print("enter all the fields")
  
  while  not name or not email or not age:
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    age = int(input("Enter your age : "))
    
    if(name and age and email):
        print(f"Name: {name}")
        print(f"age: {age}")
        print(f"email: {email}")
        break;  
print(f"Name: {name}")
print(f"age: {age}")
print(f"email: {email}")