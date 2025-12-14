def right(arr, n, d):  
    temp = arr[n-d:]  
    for i in range(n-d-1, -1, -1):   
        arr[i+d] = arr[i]
    for i in range(d):   
        arr[i] = temp[i]
    return arr
arr = [1,2,3,4,5,6,7]
d = 3
n = len(arr)
print(right(arr, n, d))