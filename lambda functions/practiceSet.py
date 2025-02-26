number = int(input("Enter a number: "))

primeNumber = lambda i, n: n % i == 0  

isPrime = True 
for i in range(2, int(number ** 0.5) + 1):  
    if primeNumber(i, number):
        isPrime = False 
        break

if isPrime and number > 1:  # 1 is not a prime number
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
