def knapSack(w,wt,val,n):
    if n==0 or w==0:
        return 0
    if t[n][w] != -1:
        return t[n][w]

    #choice for each ele. 0/1
    if wt[n-1]>w:
        t[n][w] = knapSack(w,wt,val,n-1)
        return t[n][w]
    t[n][w] = max(val[n-1]+knapSack(w-wt[n-1],wt,val,n-1),knapSack(w,wt,val,n-1))
    return t[n][w]

val=[20,30,10,50]
wt=[1,3,4,6]
w=10
n = len(val)
t = [[-1 for i in range(w+1)] for j in range(n+1)]
print(t)


print(knapSack(w,wt,val,n))
print(t)