def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

n=int(input())
k=0
m=n+1
while True:
    if prime(m):
        break
    m+=1
print(m)
