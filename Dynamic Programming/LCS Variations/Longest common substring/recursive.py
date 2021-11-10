def LCSubstring(x,y,n,m,count):
    if n == 0 or m == 0:
        return count

    if x[n-1] == y[m-1]:
        count = LCSubstring(x,y,n-1,m-1,count + 1)
    count = max((count,max(LCSubstring(x,y,n,m-1,0), LCSubstring(x,y,n-1,m,0))))
    return count
print(LCSubstring(["a","b","c","d","g","h"],["a","b","e","d","f","h","r"],6,7,0))