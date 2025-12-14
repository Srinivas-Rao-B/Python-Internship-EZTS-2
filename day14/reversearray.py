def reverse_array(arr):
    stack=[]
    for e in arr:
        stack.append(e)
    for i in range(len(arr)):
        arr[i]=stack.pop()
    return arr
arr=list(input().split())
print(reverse_array(arr))