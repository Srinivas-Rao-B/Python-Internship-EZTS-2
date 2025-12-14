# st=[]
# st=input().strip()
# l=len(st)
# count=0
# for i in st:
#     max=0
#     for j in st:
#         if i==j:
#             max+=1
#     if max>count:
#         count=max
# print(l-count)

#abcdabc a 2 times b 2 times c 2 times d 1 time, max is 2, return total len - max == 7-2=5
s={}
n=[]
n=input().strip()
s=n
x=[]
for i in s:
    if i not in x:
        x.append(s.count(i))
k=max(x)
print(len(n)-k)