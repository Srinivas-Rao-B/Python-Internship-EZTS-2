n=int(input())
x=list(map(int,input().split()))
x=x[:n]
max=x[0]
min=x[0]
l=len(x)
for i in range(l):
    if x[i]>max:
        max=x[i]
    elif x[i]<min:
        min=x[i]
print(min+max)