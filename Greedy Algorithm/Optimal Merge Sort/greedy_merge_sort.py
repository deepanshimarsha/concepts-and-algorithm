#1 sort lists by sizes(more than 2 sorted lists)
#2 merge two smallest size lists

def optimalMergeSort(arr):
    sort_arr = sorted(arr, key=len)
    if len(sort_arr) == 1:
        return sort_arr[0]
    new_arr = mergesort(sort_arr[0],sort_arr[1])
    sort_arr.append(new_arr)
    return optimalMergeSort(sort_arr[2:])
    
def mergesort(arr1, arr2):
    arr = []
    i,k = 0,0
    while i < len(arr1) and k < len(arr2):
        if arr1[i] >= arr2[k]:
            arr.append(arr2[k])
            k += 1
        elif arr1[i] < arr2[k]:
            arr.append(arr1[i])
            i += 1

    if i >= len(arr1):
        while k < len(arr2):
            arr.append(arr2[k])
            k += 1
    elif k >= len(arr2):
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1

    return arr

print(optimalMergeSort([(1,4,8,12,16,20),(3,6,9,12,15),(2,4),(5,10,15)]))