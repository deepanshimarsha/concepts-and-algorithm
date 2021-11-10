x = ["a","b","c","d","g","h"]
y = ["a","b","e","d","f","h","r"]
n, m = len(x), len(y)
memo = [[-1 for i in range(m+1)] for j in range(n+1)]

def LCS(x,y,n,m):
    if n == 0 or m == 0:
        return 0

    if memo[n][m] != -1:
        return memo[n][m]

    if x[n-1] == y[m-1]:
        memo[n][m] =  1 + LCS(x,y,n-1,m-1)
        return memo[n][m]
    else:
        memo[n][m] = max(LCS(x,y,n-1,m),LCS(x,y,n,m-1))
        return memo[n][m]

print(LCS(x,y,n,m))