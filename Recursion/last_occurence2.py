def function(arr, size,idx,val,x):
    if idx == size:
        return x
    if arr[idx] == val:
        x = idx
    return function(arr, size, idx+1, val,x)
   
print(function([3,5,7,2,4,5],6,0,5,-1))



     
    