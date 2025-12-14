n=int(input()) #range for square and cube
count=0
max=0
for i in range(1,n+1):
    s=i*i
    if s<=n:
        if s>count:
            count=s
    j=i*i*i
    if j<=n:
        if j>max:
            max=j
print(count+max)