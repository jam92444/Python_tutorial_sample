#identity operator to verify the thing is same.


# 1. is operator is used to return true or false by verifying the value is same of difference.
# x = 10
# y = 20 
# z = 10
# print("is: ",x is y) #return  boolean 
# print("is: ",x is z) #return  boolean 


# # 2. is not operator is used to return true or false by verifying the value is not same of difference.
# # x = 10
# # y = 20 
# # z = 10
# # print("is not: ",x is not y) #return  boolean 
# # print("is not: ",x is not z) #return  boolean   

# x = int(input("Enter x"))
# y = int(input("Enter y"))
# if x is y :
#     print(True);
# else:
#     print(False);
    

#Membership operator

#1. In Operator - used to check the existance of the given value. 

list1 = ["apple","mango","banana"];

# print("mango" in list1) #if the string value mango is exist in list1.Ture.

# for x in list1:
#     if x == "mango":
#         print(True)
#     else:
#         print(False)


#2.Not in Operator - used to check the value is not  in given list or collection. 

list2 = ["apple","mango","banana"];

print("mango" not in list2) #if the string value mango is not exist in list2.Ture. otherwise false.