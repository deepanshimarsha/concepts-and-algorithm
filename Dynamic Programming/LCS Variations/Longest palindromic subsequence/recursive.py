def LPS(arr1,n):
    arr2 = arr1[::-1]
    print(arr2)
    m = len(arr2)
    return LCS(arr1,arr2,n,m)

def LCS(x,y,n,m):
    if n == 0 or m == 0:
        return 0 
    if x[n-1] == y[m-1]:
        return 1 + LCS(x,y,n-1,m-1)
    else:
        return max(LCS(x,y,n-1,m),LCS(x,y,n,m-1))

print(LPS(["a","g","b","c","b","a"],6))