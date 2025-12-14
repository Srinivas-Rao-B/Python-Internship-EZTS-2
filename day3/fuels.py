n=int(input()) 
p=int(input())
q=int(input())
r=n//80
b=r*p*75
k=r*80
i=n-k
if i>0:
    s=i/8
    s1=int(s)
    if s!=s1:
        s1+=1
    sk=s1*q*75
    b+=int(sk)
print(b)
#n is total people, 80 is capacity of people in 1 bus, 8 people in 1 shuttle capacity,75 is fule rate, p,q is total liter of fuel