l=[]
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
l=list(map(str,input("Enter the message:").strip()))
k=int(input("Enter the key:"))
x=[]
for i in range(len(l)):
    if l[i]==" ":
        print(" ",end="")
    else:
        for j in range(len(a)):
            if l[i]==a[j]:
                y=j
        print(a[y+k-26],end="")

# l=[]
# l=list(map(str,input("enter the message:").strip()))
# k=int(input("Enter the key:"))
# x=[]
# for i in l:
#     if i==" ":
#         x.append(" ")
#     else:
#         x.append(chr(ord(i)+k))
# print("".join(x))