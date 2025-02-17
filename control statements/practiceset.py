# 1. Python program to print all the even numbers within the given range.

# if the given range is 10 
'''
given_range = int(input("Enter range: "));
 
 
given_range = given_range+1
for i in range(1,given_range):
    # if number is divisble by 2
    # then it's even
    if i%2==0:
            # if above condition is true
            # print the number
            print("even : ",i);      
    else:
            print("Odd  : ",i);

#2: Python program to calculate the sum of all numbers from 1 to a given number.

# Getting run time input
number = int(input("Enter number: "));

#adding 1 to run till the desire range
number=number+1;

# initial value of sum before addition
sum =0;

# looping each number and adding into the sum 
for i in range(1,number):
    
    sum=sum+i;
    
# returning the result
print(f"sum of 1 to {number-1} is {sum}.");

# Output

Enter number: 12
sum of 1 to 12 is 78.



#3 : Python program to calculate the sum of all the odd numbers and all the even number within the given range
# Getting run time input
number = int(input("Enter number: "));

#adding 1 to run till the desire range
number=number+1;

# initial value of sum before addition
even_sum =0;
odd_sum =0;

# looping each number and adding into the sum 
for i in range(1,number):
    if (i%2==0):
        even_sum=even_sum+i;
    else:
        odd_sum=odd_sum+i;
    
# returning the result
print(f"Sum of even from 1 to {number-1} is {even_sum}.");
print(f"Odd of odd from 1 to {number-1} is {odd_sum}.");


#4. Python program to print a multiplication table of a given number


#taking runtime input 
table = int(input("Enter the table: "));
print(f"Table for {table}.")
# iteration for 10 times. 
for i in range(10):
    i=i+1; # adding i+1 because i initally starts with zero. so by addin 1 its starts with 1. 
    print(f"{table} X {i} = {table*i}"); # simply multiplying. 
    
#output
Enter the table: 12
Table for 12.
12 X 1 = 12  
12 X 2 = 24  
12 X 3 = 36  
12 X 4 = 48  
12 X 5 = 60  
12 X 6 = 72  
12 X 7 = 84  
12 X 8 = 96  
12 X 9 = 108 
12 X 10 = 120



#5. Python program to display numbers from a list using a for loop.

#list is given
list = [1,2,4,6,88,125]

#iterating each value i carry value from a list 
for i in list:
    print(i)
    
#Output

1
2
4
6
88
125


#6: Python program to count the total number of digits in a number.

#method 01
#runtime input and getting as a string because using int value we cannot get the length but the 
number = input("Enter you number: ");

#using len() we can get the length of the string
print("Length of given number: ",len(number))

#method 02 
length = 0 
for i in range(1,len(number)+1):
    length = length+1
print("Length of given number: ",length)


#output
# Enter you number: 13234523124435
# Length of given number:  14

# 7. Python program to check if the given string is a palindrome.
#input 
#INPUT REVERSE
#INPUT == REVERSER EQUAL IS PALINDROME ELSE NOT PALINDROME

word = input("Enter your work: "); #madan

reverse = "";

for i in word:
    reverse = i + reverse # reverse= m +"" # reverse = a + m # reverse(am) = d+am=dam; #reverse = a + dam = adam #reverse=n+adam= nadam; madan==nadam

if(word == reverse):
    print(f"you word {word} is a palindrome");
else:
    print(f"you word {word} is not a palindrome");
    
#output-1
Enter your work: non
you word non is a palindrome
#output-2
Enter your workbushra
you word bushra is not a palindrome   


8.Python program that accepts a word from the user and reverses it.
9. Python program to check if a given number is an Armstrong number
10.Python program to display all numbers within a range except the prime numbers.
11.Python program to get the Fibonacci series between 0 to 50.
12. Python program to find the factorial of a given number.
13.Python program that accepts a string and calculates the number of digits and letters.
14.Write a Python program that iterates the integers from 1 to 25.
15.Python program to check the validity of password input by users.
16.Python program to convert the month name to a number of days.
17.Write a Python program that iterates the integers from 1 to 25.
'''

a = 10 
b = 20

def add(a,b):
    print(a+b)
def add2(a,b):
    print(a+b)

add(11,2)