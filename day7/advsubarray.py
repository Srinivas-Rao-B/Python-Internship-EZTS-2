n=int(input())#5
k=int(input())#2
arr=list(map(int,input().split()))# 1 2 3 4 5
mx=-1
for i in range(0,len(arr)-k+1):
    temp=arr[i:i-k]
    k=1
    s=0
    for j in temp: 
        s+=(j*k)
        k+=1
        if(s>mx):
            mx=s
print(mx)