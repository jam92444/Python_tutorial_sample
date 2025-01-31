# #List operations 

# thislist = ["apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry"]
# # print(thislist[1])

# #list length using len() 

# print(len(thislist))


# # checking type 

# print(type(thislist))

    # list constructor
    # list2 = list((1,2,3,4,5,7),(1,2,3,4,5,6))
    # print(list2)

# #                   0-n                 -3,-2,-1
# #Accessing the list [1,2,3,4,558,6,7,,9]
# print(thislist[6:-2])


# '''
# front
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15...n]
# [1,2,4,5,6,9,[2,4,8,9,0,6,3,2,4,6,[7,8,9],0]
# back    
# [-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

# '''

# #negative index
# print(thislist[-4:-1])

#range of index

#Check if Item Exists

list1 = ["apple","mango","orange","banana"];

if "apple" in list1:
    print(True) 

#changing value in a list.

list1[1] = "mango2";

print("Adding: ", list1)

# adding value in a list using append(value) 

list1.append(2);
list1.append(4);
print("Append: ",list1)

#inserting a value in a list using insert(position,value);
list1.insert(1,4)
print("Insert: ",list1)

#remove the value from a list using remove(value).
list1.remove(4);
print("Remove: ",list1)

#pop will remove value from a certain position in a list using pop(position) methods
list1.pop(-1);
print("Pop: ",list1)
list1.pop();
print("Pop without value: ",list1)

#list looping

# for listitem in list1: #for listitem='apple' in list1,listitem="mango2" in list1
#     print(listitem) #0  

'''
for value in list1

#BHS
['apple', 'mango2', 'orange', 'banana']
len(lsit1)

for (i=0,i<len(list1),i++)
    print(list1[i])
    
    first loop
    
      i=0  ,0<4,0+1
for (i=0,i<len(list1),i++)
    print(list1[i]) //list1[i] print(apple)
    
    
    second loop
    
      i=1,1<4,1+1
for (i=0,i<len(list1),i++)
    print(list1[i]) //list1[1] print(mango2)
    
    third loop
    
      i=2,2<4,2+1
for (i=0,i<len(list1),i++)
    print(list1[i]) //list1[2] print(orange)
    
    fourth loop
    
      i=3,3<4,3+1
for (i=0,i<len(list1),i++)
    print(list1[i]) //list1[3] print(banana)
    
    fifth loop
    
      i=4,4<4,3+1
for (i=0,i<len(list1),i++)
    print(list1[i]) //list1[3] print(banana)




'''

#using sort methods to sort the list
list1.sort()

print("Sort: ",list1)
list2 = [12,3,4,5,6,8,9,434,23];
list2.sort();
print("Sorting the number:",list2)


# copy in list . use to make a duplicate value in a new list.
list3 = list2.copy()
print(list3)

#joining the list to another list

list3 = list1 + list3;
print(list3)

#method 2
list3.extend(list2)
print(list3)