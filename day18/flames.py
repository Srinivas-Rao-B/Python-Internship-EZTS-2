str1=[]
str2=[]
print("FLAMES Game")
print("Enter 1st name:")
str1=list(map(str,input().strip()))
print("Enter 2nd name:")
str2=list(map(str,input().strip()))
if ' ' in str1:
    str1.remove(' ')
if ' ' in str2:
    str2.remove(' ')
for i in str1[:]:
    if i in str2:
        str1.remove(i)
        str2.remove(i)
count=len(str1)+len(str2)
if count==0 or count%6==0: # F L A M E S   
    print("Siblings")
elif count%6==1:
    print("Friends")
elif count%6==2:
    print("Love")
elif count%6==3:
    print("Affection")
elif count%6==4:
    print("Marriage")
elif count%6==5:
    print("Enemy")