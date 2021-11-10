def tribonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return n-1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print(tribonacci(5))