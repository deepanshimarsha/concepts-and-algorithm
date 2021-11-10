def function(arr, size, idx, val):
    if idx == size:
        return -1
    elif arr[idx] == val:
        return idx
    return function(arr, size, idx+1, val)

print(function([3,7,5,2,4,5], 6, 0, 5))