def find_winner(n, votes):
    if n == 1:
        return votes[0]
    candidate, count = None, 0
    for v in votes:
        if count == 0:
            candidate, count = v, 1
        elif candidate == v:
            count += 1
        else:
            count -= 1
    if votes.count(candidate) > n // 2:
        return candidate
    else:
        return -1
n = int(input())                    
votes = list(map(int, input().split()))  
print(find_winner(n, votes))
#6
#1 2 1 1 2 2 