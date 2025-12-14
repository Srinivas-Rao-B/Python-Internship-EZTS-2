x=[] #philipBULB
x=list(input().strip())
l=len(x)
for i in range(l):
    if x[i]>='A' and x[i]<='Z':
        x[i]=x[i].lower()
    elif x[i]>='a' and x[i]<='z':
        x[i]=x[i].upper()
    print(x[i],end='')