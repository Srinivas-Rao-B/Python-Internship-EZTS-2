def giveresult(s1,s2,s3):
    if s1<s2:
        print("Good")
    elif s1>=s2 and s1<=s3:
        print("Best")
    elif s1>s3:
        print("Can do Better")
s1=int(input("Enter the score of 1st level:"))
s2=int(input("Enter the score of 2nd level:"))   
s3=int(input("Enter the score of 3rd level:"))
print("The result is:")
giveresult(s1,s2,s3)