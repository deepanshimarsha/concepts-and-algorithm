#no of ways
def CoinChange(arr,n,Sum,):
    if Sum == 0:
        return 1
    elif n == 0  and Sum > 0:
        return 0

    #choice diagram
    if arr[n-1] > Sum:
        return CoinChange(arr,n-1,Sum)
    else:
        return CoinChange(arr,n,Sum-arr[n-1]) + CoinChange(arr,n-1,Sum)

arr = [1,2,3]
n = len(arr)
Sum = 5
print(CoinChange(arr,n,Sum))
