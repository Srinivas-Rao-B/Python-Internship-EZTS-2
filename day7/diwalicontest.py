n=int(input())#6
p=int(input())#180
s=0
count=0
for i in range(1,n+1):
    s+=5*i
    if s<=(4*60-p):
        count+=1
print(count)