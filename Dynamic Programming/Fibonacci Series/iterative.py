#bottom-up approach
def fib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(2,n+1):
        table[i] = table[i-2] + table[i-1]

    return table[n]

print(fib(5))