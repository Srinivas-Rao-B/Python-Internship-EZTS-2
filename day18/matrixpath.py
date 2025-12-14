row=int(input("Enter the number of rows:"))
col=int(input("Enter the number of columns:"))
matrix=[[0]*col for i in range(row)]
count=0
for i in range(0,row):
    for j in range(0,col):
        matrix[i][j]=int(input())
        if matrix[i][j]==1:
            count+=1
print(count)