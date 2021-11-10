def function(arr, idx, val):
    if idx == 0:
        return -1
    elif arr[idx] == val:
        return idx
    return function(arr, idx-1, val)

print(function([3,5,7,5,2,4], 5, 5))
