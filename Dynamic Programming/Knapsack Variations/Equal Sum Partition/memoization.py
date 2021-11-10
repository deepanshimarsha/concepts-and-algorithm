def equalpartition(arr,n):
    arr_sum = sum(arr)

    #cond for equal partition
    if (arr_sum % 2) != 0:
        return False
    else:
        s = arr_sum//2
        memo = [[-1 for i in range(s+1)] for j in range(n+1)]
        return subsetsum(arr,n,s,memo)
    
def subsetsum(arr,n,s,memo):
    #base cond
    if n >= 0 and s == 0:
        return True
    elif n == 0 and s > 0:
        return False

    #check
    if memo[n][s] != -1:
        return memo[n][s]   

    #choice diagram
    #store
    if s < arr[n-1]:
        memo[n][s] = subsetsum(arr,n-1,s,memo)
        return memo[n][s]
    else:
        memo[n][s] = subsetsum(arr,n-1,s,memo) or subsetsum(arr,n-1,s-arr[n-1],memo)
        return memo[n][s]

arr = [1,5,11,5]
n = len(arr)

print(equalpartition(arr,n))