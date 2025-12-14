x=[] # 5667788 5
x= list(input().strip())
count=0
l=len(x)
y=x[l-1]
for i in range(l-2):
    if x[i]!=y:
        count+=1
print(count)