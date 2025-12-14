n=int(input()) #array size
x=input().split() #array ele positive and negative
x=[int(i) for i in x]
x=x[:n]
count=0
for i in x:
    if i>0:
        count+=1
print(count)