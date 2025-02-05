
usersData = []

name = input("Enter your name: ");
age = int(input("Enter your Age: "));
line1 = input("Enter your address line1 : ");
line2 = input("Enter your address line2 : ");
pincode = int(input("Enter your Pincode: "));
city = input("Enter your city : ");
state = input("Enter your state: ");

biodata = {
    "name":name,
    "age":age,
    "address":{
        "line1":line1,
        "line2":line2,
    },
    "pincode":pincode,
    "city":city,
    "state":state,
};
biodata2 = {
    "name":name,
    "age":age,
    "address":{
        "line1":line1,
        "line2":line2,
    },
    "pincode":pincode,
    "city":city,
    "state":state,
};
usersData.append(biodata)
usersData.append(biodata2)

print("For loop running ")

for x in usersData:
    if x['name'] == "bushra":
        print("This is the person we are looking for .")
        print("Name: ",biodata["name"])
        print("Age: ",biodata["age"])
        print("Address: ",biodata["address"]["line1"],biodata["address"]["line2"])
        print("pincode: ",biodata["pincode"])
        print("city: ",biodata["city"])
        print("state: ",biodata["state"])
            
    
    
print("For loop end")

