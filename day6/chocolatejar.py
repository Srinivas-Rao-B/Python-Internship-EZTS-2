def chocolates_for_A(arr, n):
    total = 0
    for jar in arr:
        total += jar // 3   
        if jar % 3 > 0:     
            total += 1
    return total
arr = list(map(int, input().split()))  
n = int(input())                       
print(chocolates_for_A(arr, n))
# 10 20 30
# 3