def power(n, k):
    if k > 0:
        return n* power(n, k-1)
    else:
        return 1

print(power(2,3))