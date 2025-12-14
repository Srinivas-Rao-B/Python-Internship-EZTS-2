print("Enter list values followed by spaces:")
lis=list()
lis=list(map(int,input().split()))
def linearsearch(lis,n):
    for i in lis:
        flag=0
        if i==target:
            flag=1
            s=lis.index(i)
            break
    if flag:
         print("Element found at index ",s,' , position ',s+1)
    else:
        print("No such element found")
        
print(lis)
print("Enter target:")
target=int(input())
n=(linearsearch(lis,target))