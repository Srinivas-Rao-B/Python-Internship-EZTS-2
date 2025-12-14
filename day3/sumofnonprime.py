n=input() #567836
x=[int(i) for i in n]
sum=0
for i in x:
    flag=1
    for j in range(2,int(i/2)+1):
        if i%j==0:
            flag=0
            break
    if flag==0:
        sum=sum+i
print(sum)