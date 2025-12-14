n=int(input())
count=0
x=0
for i in range(1,n+1):
    max=0
    x=i
    print(" "*(n-i),end="")
    for j in range(i):
        while x!=1:
            max+=x
            print(x,end="")
            x=x-1
    print(1,end="")
    if i>1:
        max*=2
        y=2
        while y<=i:
            print(y,end="")
            y+=1
    max+=1
    print()
    count+=max
print(count)


# m=n
# sum=0
# for i in range(1,m+1):
#     print("  "*(m-i),end="")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#         sum+=j
#     for k in range(2,i+1):
#         print(k,end=" ")
#         sum+=k
#     print()
# print("sum=",sum)
