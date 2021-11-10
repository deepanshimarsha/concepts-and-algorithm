#top-down approach
def fib(n, memo):
    if n<= 1:
        memo[n] = n
    if n not in memo:
        memo[n] = fib(n-2, memo) + fib(n-1, memo)
    return memo[n]
        

n = 5
memo = [None]*(n+1)
print(fib(n,memo))

