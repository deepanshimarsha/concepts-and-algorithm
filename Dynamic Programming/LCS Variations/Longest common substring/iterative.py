def LCS(x,y,n,m):
    memo = []
    for i in range(n+1):
        memo.append([0])
    for j in range(1,m+1):
        memo[0].append(0)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                memo[i].append(1 + memo[i-1][j-1])
            else:
                memo[i].append(0)
    print(memo)
    lst = [max(memo[i]) for i in range(0,n+1)]
    print(lst)
    return max(lst)
    

print(LCS(["a","b","c","d","g","h"],["a","b","e","d","f","h","r"],6,7))