def rodcutting(length, val,n,rod):
    if n == 0 or rod == 0:
        return 0
    if memo[n][rod] != -1:
        return memo[n][rod]
    if length[n-1] <= rod:
        memo[n][rod] = max(rodcutting(length,val,n-1,rod), val[n-1] + rodcutting(length,val,n,rod-length[n-1]))
    else:
        memo[n][rod] = rodcutting(length,val,n-1,rod)
    return memo[n][rod]

length = [1,2,3,4,5,6,7,8]
val = [1,5,8,9,10,17,17,20]
n = 8
rod = 8
memo = [[-1 for i in range(rod+1)] for j in range(n+1)]
print(rodcutting(length, val,n,rod))