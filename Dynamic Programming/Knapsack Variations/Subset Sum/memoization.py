def subsetsum(arr,n,sum):
    #base cond
    if n >= 0 and sum == 0:
        return True
    elif n == 0 and sum > 0:
        return False

    #check before recursion
    if memo[n][sum] != -1:
        return memo[n][sum]

    #choice diagram
    #store in memo
    if sum < arr[n-1]:
        memo[n][sum] = subsetsum(arr,n-1,sum)
        return memo[n][sum]
    else:
        memo[n][sum] = (subsetsum(arr,n-1,sum) or subsetsum(arr,n-1,(sum-arr[n-1])))
        return memo[n][sum]
    
arr = [2,3,7,8,10]
n = 5
sum = 11
memo = [[-1 for i in range(sum+1)] for j in range(n+1)]      
print(subsetsum(arr,n,sum))
 