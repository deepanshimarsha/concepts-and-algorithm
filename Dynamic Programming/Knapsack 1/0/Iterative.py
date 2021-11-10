def knapsack(n, w, v, capacity):
    arr = []
    for i in range(0,n+1):
        arr.append([0])
    #print(arr)
    for j in range(1,capacity+1):
        arr[0].append(0)
    #print(arr)

    for i in range(1,n + 1):
        for j in range(1,capacity + 1):
            if j < w[i-1]:
                arr[i].append(arr[i-1][j])
            else:
                arr[i].append(max(arr[i-1][j], v[i-1] + arr[i-1][j-w[i-1]]))
            #print(arr[i][j])

    #print(n,capacity)
    return arr[n][capacity]

print(knapsack(4, [1,3,4,6],[20,30,10,50],10))
    
