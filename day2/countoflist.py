lis=list(input().split())# cat cat latt latt bat cat latt bat bat
n=int(input()) #3(more than 3 times repesting)
x=list()
l=len(lis)
for i in range(l):
    count=0
    for j in range(l):
        if lis[i]==lis[j]:
            count+=1
    if count>=n:
        if lis[i] not in x:
            x.append(lis[i])
l2=len(x)
for i in range(l2):
    print(x[i],end=' ')