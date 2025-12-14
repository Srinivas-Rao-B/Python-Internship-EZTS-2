# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))

# print("Enter the elements of the matrix row-wise:")
# matrix = []
# for i in range(row):
#     r = list(map(int, input().split()))
#     matrix.append(r)

# max_row_sum = max(sum(r) for r in matrix)

# max_col_sum = 0
# for c in range(col):
#     col_sum = sum(matrix[r][c] for r in range(row))
#     if col_sum > max_col_sum:
#         max_col_sum = col_sum
# print("Maximum sum of rows and columns:", max_row_sum + max_col_sum)

col=int(input("Enter the number of columns:"))
row=int(input("Enter the number of rows:"))
num=[[0]*col for i in range(row)]
for i in range(row):
    for j in range(col):
        num[i][j]=int(input(f"Enter the value of {i+1} row and {j+1} column:"))
max_row_sum=0
max_col_sum=0
for i  in range(row):
    sum=0
    for j in range(col):
        sum+=num[i][j]
    if sum>max_row_sum:
        max_row_sum=sum
for i in range(col):
    sum=0
    for j in range(row):
        sum+=num[j][i]
    if sum>max_col_sum:
        max_col_sum=sum
print(max_row_sum+max_col_sum)