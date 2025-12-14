arr=list(map(int,input().split()))
count=0
sum=0
n=len(arr)
for i in range(n):
    sum+=arr[i]
    if(sum==0):
        count+=1
print(count)