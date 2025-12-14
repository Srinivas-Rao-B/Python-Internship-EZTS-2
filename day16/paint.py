inp=int(input("Enter the interior walls:"))
out=int(input("Enter the outer walls:"))
sum=0
for i in range(1,inp+1):
    n=float(input("Enter square feet of interior wall:"))
    sum+=n*18
print("Interior cost:",sum)
sum2=0
for j in range(1,out+1):
    m=float(input("Enter square feet of outer wall:"))
    sum2+=m*12
print("Exterior cost:",sum2)
print("Total cost of painting:",sum+sum2)
