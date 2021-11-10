#minimum no of coins
import sys
def CoinChange(arr, n, s):
    #base case
    if n == 0  and s >= 0:
        return sys.maxsize - 1
    elif n > 0 and s == 0:
        return 0
    if n == 1 and s > 0:
        if s % arr[0] == 0:
            return s // arr[0]
        else:
            return sys.maxsize - 1
    
    #choice diagram
    if arr[n-1] > s:
        return CoinChange(arr, n-1,s)
    else:
        return min(1 + CoinChange(arr,n,s-arr[n-1]),CoinChange(arr,n-1,s,))

arr = [1,3,1,4]
n = len(arr)
s = 5
print(CoinChange(arr,n,s))