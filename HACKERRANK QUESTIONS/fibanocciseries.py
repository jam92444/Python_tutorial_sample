# def fibanocci(n):
#     if n<=1:
#         return n;
    
#     return fibanocci(n-1)+ fibanocci(n-2);

# print(fibanocci(5))


num =3

numb1 = 0
numb2 =1 
next_number = numb2;
count = 1;

while count <=num:
    print(next_number,end=" ");
    count+=1;
    
    numb1,numb2 = numb2,next_number;
    
    next_number = numb1 + numb2;



    
    