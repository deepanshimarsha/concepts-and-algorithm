def LCS(x,y,n,m):
    if n == 0 or m == 0:
        return 0 
    if x[n-1] == y[m-1]:
        return 1 + LCS(x,y,n-1,m-1)
    else:
        return max(LCS(x,y,n-1,m),LCS(x,y,n,m-1))

print(LCS(["a","b","c","d","g","h"],["a","b","e","d","f","h","r"],6,7))