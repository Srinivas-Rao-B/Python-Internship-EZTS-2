n=int(input("Enter the size of array:"))
a=[]
print("Enter the elements of size ",n," :")
a=list(map(int,input().split()))
even=[]
odd=[]
def sort(a):
    even=[]
    odd=[]
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
even,odd=sort(a)
for i in range(len(even)):
    print(even[i],end=" ")
for i in range(len(odd)):
    print(odd[i],end=" ") 