n=153
x=[]
x=list(map(int,str(n)))
s=0
for i in range(len(x)):
    s=s+x[i]**3
if s==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")