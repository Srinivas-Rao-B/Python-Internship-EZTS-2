sum=int(input())
if sum>9:
    while sum>9:
        i=sum%10
        sum=int(sum/10)
        sum+=i
print(sum) #345= 3+4+5 =12 =2+1 =3