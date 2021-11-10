def partition(arr,low,high):
    pivot_index = high
    pivot = arr[high]
    #start = low-1
    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if(low < high):
            arr[low], arr[high] = arr[high], arr[low]
      
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return high

def quicksort(low,high,arr):
    if low < high:
        pi = partition(arr,low,high)

        quicksort(low,pi-1,arr)
        quicksort(pi+1,high,arr)

array = [ 10, 7, 8, 9, 1, 5 ]
quicksort(0, len(array) - 1, array)
  
print(f'Sorted array: {array}')
