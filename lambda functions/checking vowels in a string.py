vowels = ['a','e','i','o','u'];

string = input("Enter a string: ");

isAvailable = lambda a,b: a == b; #return true when both are same otherwise return false

charTrue = []; #store vowel 

for char in vowels: #e
    for strin in string: #hello 
        isTrue = isAvailable(strin,char); #lambda(e,e)
        if isTrue:
            if strin not in charTrue:
                charTrue.append(strin);
     

if len(charTrue) > 0:
    print(len(charTrue),charTrue);
else:
    print("no vowels found");
