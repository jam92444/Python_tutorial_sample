# # dictionary is nothing but a type which contain key pair values. And it is the one of the most used typein in every lang. 

# #how create dict
# biodata = {
#     'name':"Bushra",
#     'age':12,
#     'gender':"Female",
#     'address':"address",
#     'fathername':"FN",
#     'mothername':"MN",
#     'income':100934023,
# }

# #accessing the data from the dict
# print("Name: ",biodata["name"])
# print("age: ",biodata["age"])
# print("gender: ",biodata["gender"])
# print("address: ",biodata["address"])
# print("fathername: ",biodata["fathername"])
# print("mothername: ",biodata["mothername"])
# print("income: ",biodata["income"])
# print(type(biodata))

# biodata2 = {
#     'name':"Bushra",
#     'age':12,
#     'gender':"Female",
#     'subject':{
#         'C++':56,
#         "python":32,
#         "java":45,
#     },
    
# }

# print(biodata2['subject']['python'])

#method 2 to createdict using constructor 
# thisdict = dict(name = "John", age = 36, country = "Norway")
# # print(thisdict)
# #key 
# print(thisdict.keys())
# #values 
# print(thisdict.values())

# @app.route('/login')
# def login():
#     # data = request.get(); #username,email,password
#     username = request.get(['username'])
#     email = request.get(['email'])
#     password = request.get(['password'])
    
#     userdata ={
#         "username":username,
#         "password":password,
#         "email":email
#     }
    
#     db.save(userdata)


# changing the dictionary
# thisdict = dict(name = "John", age = 36, country = "Norway")

# thisdict["name"] = "bushra";

# print(thisdict)


# Update the "year" of the car by using the update() method:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # thisdict.update({"year": 2020})
# # print(thisdict)
# # '''
# # varnamex.update({key:value})

# # '''

# # Add a value in hte dictionary
# thisdict["color"] = "red"

# print(thisdict)


#pop() it will remove the specifed key value

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

#popitem() it willremove the last added key pair values
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# #The del keyword removes the item with the specified key name:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # # del thisdict["model"]
# # # print(thisdict)
# # del thisdict
# # print(thisdict)


# #looping the key pair values in dictionary 
# # for x in thisdict:
# #     print(thisdict[x])
# # for x in thisdict.values():
# #     print(x)
# for x in thisdict.keys():
#     print(f'{x} :  {thisdict[x]}')

# orange = {
#     "mens":[1,2,3,4]
# }

# for a in orange["mens"]:
#     print(a)