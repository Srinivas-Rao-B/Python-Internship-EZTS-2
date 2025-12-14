n=int(input())#2
x=int(input())#3
r=int(input())#100  output 2*3*3*3.... until range 100 and output as {2,6,18,54}
res=n
k=list()
k.append('{')
k.append(n)
while res<r:
    res*=x
    if res<=r:
        k.append(',')
        k.append(res)
k.append('}')
for i in k:
    print(i,end='')