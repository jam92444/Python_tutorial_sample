#accessing the set values

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
  
# checking the specific value existance
# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)


# thisset = {"apple", "banana", "cherry"}

# print("banana" not in thisset)

# Adding value in the sets. 
# thisset = {"apple", "banana", "cherry"}
# thistuple = ("apple", "banana", "cherry")

# thisset.add("orange")
# print(thisset)
# thistuple.add("orange")
# print(thistuple)

# Update set in the current sets 

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)
# print(thisset)


# #nothing
# print(thisset)


# Adding any iterables in the sets using Update methods
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# remove () methods  to remove item from the set syntax:- a.remove(value) or we can use discard methods
# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)

# thisset.discard("apple")

# print(thisset)

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop() #banana

# print(x) #banana

# print(thisset)

#Clear - clear() methods use to empty the data. ?..add()
# thisset = {"apple", "banana", "cherry"} 

# thisset.clear()
#methods methosname()
# # ex del
# del thisset

# print(thisset)

'''

Join Sets

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
    
'''

# Union
# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set4 = set1 | set2;
print(set4)
# You can use the | operator instead of the union() method, and you will get the same result.