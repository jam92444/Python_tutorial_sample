
'''
Q: Print the list in lexicographic increasing order.
    SAMPLE INPUT 
    1
    1
    1
    2
    
    SAMPLE OUTPUT
    
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [];

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                coordinates.append([i,j,k]);

print(coordinates)