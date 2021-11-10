def MaxlenChain(arr,n):
    memo = [1]*n
    for i in range(1,n):
        j = 0
        while i > j:
            if list(arr[i])[0] > list(arr[j])[1]:
                memo[i] = max(memo[i],memo[j] + 1)
            j += 1
    print(memo)
    return max(memo)

print(MaxlenChain([[5,24],[39,60],[15,28],[27,40],[50,90]],5))
