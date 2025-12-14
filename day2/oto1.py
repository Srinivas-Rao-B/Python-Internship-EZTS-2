print("Enter input:")
ch=[]
ch=list(input().strip())
l=len(ch)
for i in range(l):
    if(ch[i]=='0'):
        ch[i]='1'
    print(ch[i],end='')# list 0 to 1


print("\nEnter a number:")
b=input()
for i in b:
    if i=='0':
        i='1'
    print(i,end='')#string tuple


print("\nEnter a number:")
num=int(input()) #id str the convert it to int. as s=int(num)
res=0
place=1 #units tens ones etc
while num>0:
    r=num%10 #remainder
    if r==0:
        r=1
    res=r*place+res
    place*=10
    num//=10
print(res) #using integer and modulus

num=input("Enter a number")
print(num.replace("0","1")) #using replace function