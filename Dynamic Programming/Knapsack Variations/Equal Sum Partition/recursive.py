def equalpartition(arr,n):
    s = sum(arr)

    #cond for equal partition
    if (s % 2) != 0:
        return False
    else:
        return subsetsum(arr,n,s//2)
    
def subsetsum(arr,n,targetsum):
    #base cond
    if n >= 0 and targetsum == 0:
        return True
    elif n == 0 and targetsum > 0:
        return False

    #choice diagram
    if targetsum < arr[n-1]:
        return subsetsum(arr,n-1,targetsum)
    else:
        return subsetsum(arr,n-1,targetsum) or subsetsum(arr,n-1,targetsum-arr[n-1])

arr = [1,5,11,5]
n = len(arr)
print(equalpartition(arr,n))