arr = [5,2,3,4,1];


def sorting(arr):
    n = len(arr);
    
    for i in range(n):
        for j in range(0,n-i-1): #5-1-1 = 2
            if arr[j] > arr[j+1]:# 4>1
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr;


print(sorting(arr));
