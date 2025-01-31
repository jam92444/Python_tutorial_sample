#tuple are immutable 
#we cannot change the value 
#tuple can be create using parenthesis


#Access value using index
# a = (1,2,3,4,5,6,7,8,9);

# print("Accessig value by using only end index",a[:5])
# print("Accessig value by using only Starting index",a[5:])
# print("Accessig value by using only negative end index",a[:-5])
# print("Accessig value by using only negative Starting index",a[-5:])

#Update Tuples

'''
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

#adding value into tuple 

# a = (1,2,3,4,5,6,7,8,9);
# #type casting simply means chaging one type to another.
# x =list(a)
# x.append("hello");
# x.insert(2,"hi")
# # print()
# print("updated list",x)

# #del which use to delete the entire tuple 
# del a;
# print(a)

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# # unpacking syntax
# # (varaible) = which tuple u need to unpack 
# (x,y,z,*b) = fruits;

# print("x: ",x)
# print("y: ",y)
# print("z: ",z)
# print("b: ",b)

# (green, *tropic, pink,red) = fruits

# print("green: ",green)
# print("pink: ",pink)
# print("tropic: ",tropic)
# print("red: ",red)

# Loop Through a Tuple

# thistuple = ("apple", "banana", "cherry")

# for x in thistuple:
#   print(x)
  


# #lopping  through index
# for i in range(len(thistuple)): #range(len(thistuple)),3 for i in range(3)
#   print(thistuple[i]) #thistuple[2] apple,banana,cherry

#joining the tuples 
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# # multiplying the tuples 

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)


'''
 Tuple index() Method. 
 Tuple count() Method. 
 '''
#count will return the number of times the value exist in the tuple. 
thistuple = (1, 3, 7, 8, 7, 4, 6, 8, 5,1,1,1,1,1)

x = thistuple.count(1)

print("Count: ",x)

#index will return the first occurance of the value.
y = thistuple.index(5)

print("Index: ",y)

z = [1,2,3,4]
del z
print(z)

