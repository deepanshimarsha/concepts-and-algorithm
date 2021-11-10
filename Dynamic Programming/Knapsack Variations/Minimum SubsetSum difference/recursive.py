def MinimumDiff(arr,n,s,diff):
    if n == 0:
        return s
    
    #choice diagram
    diff = min(diff, abs((MinimumDiff(arr,n-1, s+ arr[n-1],diff) - MinimumDiff(arr,n-1,s,diff))))
    return diff

arr = [1,6,11,15]
n = 4
s = 0
diff = sum(arr)
print(MinimumDiff(arr,n,s,diff))