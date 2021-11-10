def CountSubset(arr,n,s):
    #base cond
    if s == 0:
        return 1
    elif n == 0 and s > 0:
        return 0
    
    #choice diagram
    if arr[n-1] > s:
        return CountSubset(arr,n-1,s)
    else:
        return CountSubset(arr,n-1,s) + CountSubset(arr,n-1,s-arr[n-1])

arr = [2,3,5,6,8,10]
n = len(arr)
sum = 10
print(CountSubset(arr,n,sum))
