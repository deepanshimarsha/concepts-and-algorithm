import sys
def MinimumLength(arr, n, s):
   
    #base case
    if n > 0 and s == 0:
        return 0
    elif n == 0 and s >= 0:
        return sys.maxsize-1
    
    if arr[n-1] > s:
        return MinimumLength(arr,n-1,s)
    else:
        return min(MinimumLength(arr,n-1,s), 1 + MinimumLength(arr,n-1,s-arr[n-1]))

arr = [1,2,3]
n = len(arr)
s = 5
print(MinimumLength(arr,n,s))
