# def is_armstrong(num): 
    
#     num_str = str(num); #converting into string 153
    
#     num_len = len(num_str); #length calculation power lenght
    
#     sum_square = sum(int(digit) ** num_len for digit in num_str); # 153
#     #sum_square =0
#     # for digit in num_str:
#     #   sum_square += int(digit) ** num_len
    
#     return sum_square == num;#153 == 153 true

# num = int(input("Enter the number: ")); # 153 = 153 armstrong 153 =154 is not armstrong

# armstrong = is_armstrong(num); #userinput armstrong=True

# if(armstrong): #true
#     print(f"{num} is a armstrong number");
    
# else:
#     print(f"{num} is not a armstrong number");
    

# num = [1,2,4,5];

# addition = sum(num);

# print(addition)

def sum(nums):#nums = [1,2,4,5,6,7,8]
    add = 0
    for i in nums:
        add += i;
        
    return add;#function return 

number = [1,2,4,5,6,7,8]

var = sum(number);

print(var);
