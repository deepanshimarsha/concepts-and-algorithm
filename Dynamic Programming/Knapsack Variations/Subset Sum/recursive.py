def subsetsum(arr,n,s):
    #base cond
    if n >= 0 and s == 0:
        return True
    elif n == 0 and s > 0:
        return False

    #choice diagram
    if s < arr[n-1]:
        return subsetsum(arr,n-1,s)
    else:
        return subsetsum(arr,n-1,s) or subsetsum(arr,n-1,s-arr[n-1])

arr = [1,5,11,5]
n = len(arr)
s = 11        
print(subsetsum(arr,n,s))