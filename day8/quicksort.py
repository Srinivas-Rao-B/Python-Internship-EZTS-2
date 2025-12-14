def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[i for i in arr if i<pivot]
    right=[i for i in arr if i>pivot]
    middle=[i for i in arr if i==pivot]
    return quicksort(left)+middle+quicksort(right)

arr=[3,2,5,7,9,1,6]
print(quicksort(arr))