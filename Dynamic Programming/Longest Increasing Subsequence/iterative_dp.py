#bottom-up
def LIS(arr):
    n = len(arr)
    memo = [1 for i in range(n)]
    for i in range(1,n):
        j = 0
        while i > j:
            if arr[i] > arr[j]:
                memo[i] = max(memo[i],memo[j] + 1)
            j += 1
    return max(memo)

print(LIS([1,2,3,4,5]))