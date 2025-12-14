def sort(arr):
    s=0
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            s+=1
        arr[j+1]=key
    return s,arr
arr=[5,4,3,2,1]
print(sort(arr))