# # # data types 
# # a = 10 # the variable is used to get a storage in a  memory.
# # a = 20 # the

# # print(a)

# #list 
# #creating  [ ]
# # print(list1)

# # #adding a element
# # list1.append('jamal');
# # print(list1)

# # #removing item in a list 
# # list1.remove(list1[4]);
# # print(list1)

# list1 = [1,2,4,5,6];

# list2 = [1,2,3,4,5];

# list3 = [1,2,3,4,5,6];

# list2.append(list3)
# list1.append(list2)

# # [1, 2, 4, 5, 6, [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6]]] 5
# # print(list1[-1][-1][-1])
# # print(list1[-1][-1][2])

# # task create nested list ..
# list1 = [1,2,3,4,5,6]
# list2 = [1,2,3,4,5,6]
# list3 = [1,2,3,4,5,6]
# list4 = [1,2,3,4,5,6]
# list5 = [1,2,3,4,5,6]
# list6 = [1,2,3,4,5,6]

# list6.append(list5)
# # list4.append(list6)
# list2.append(list4)
# list3.append(list2)
# combined = list3;

# print(combined)

# # combined.remove(combined[6][2])
# # print(combined)

# #sets
# #how to create set
# # to create a set we use {}

# methods 01 set
# a = {10,20,30}
# print(type(a))

# b = set([10,20,30]);
# print(b)
# print(type(b))

#dictionary

#how to create a dict

#syntax : {key:value,key:value}

# a = {
#     'one' : "hello",
#     'two' : "hi"
# }


# print(a)
# #method1
# print(a['one']);
# #method2
# print(a.get('one'))
# print(a.get('1'))


# Tuple 
#creating the tuple using ()

#method 1
# a = (1,2,3,4,6,7);
# print(type(a))

# #method 2
# b = tuple([10,20,30]);
# print(b)
# # b.add('3')



#task

#interger

a = 12
print(type(a))