print("Enter list values followed by spaces:")
lis=list()
lis=list(map(int,input().split()))
lis.sort()
print(lis)
print("Enter target:")
target=int(input())
def binarysearch(l,t):
    low=0
    high=len(lis)-1
    while(low<=high):
        mid=(low+high)//2
        if lis[mid]==target:
            s=mid
            print("Element found at index:",s)
            return True
        elif(target>lis[mid]):
            low=mid+1
        else:
            high=mid-1
if binarysearch(lis,target):
    print("Search Successful")
else:
    print("Element not found\nUnsuccessful search")