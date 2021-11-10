def MaximumSum(arr,n):
    memo = [0]*n
    memo[0] = arr[0]
    for i in range(1,n):
        j = 0
        while i > j:
            if arr[i] > arr[j]:
                s = arr[i] + memo[j]
                memo[i] = max(memo[i],s)
            j += 1

        if memo[i] == 0:
            memo[i] = arr[i]

    max_sum = max(memo)
    print(max_sum)
    idx = memo.index(max_sum)
    subseq = []
    subseq.append(arr[idx])
    next_idx = idx -1
    #print(next_idx)
    while next_idx >= 0:
        if memo[next_idx] == memo[idx] - arr[idx]:
            subseq.append(arr[next_idx])
            idx = next_idx
        
        next_idx -= 1
       
    return subseq

print(MaximumSum([1,101,2,3,100,4,5],7))