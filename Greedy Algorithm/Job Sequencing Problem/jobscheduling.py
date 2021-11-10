def JobScheduling(arr, n):
    slots = [0]*n
    sort_arr = sorted(arr, key=lambda x: (x[2],x[1],x[0]), reverse=True)
    print(sort_arr)
    for job in sort_arr:
        deadline = job[1]
        #print(deadline)
        for k in range(deadline-1,-1,-1):
            #print(k,deadline)
            if slots[k] == 0:
                slots[k] = job[0]
                break
    return slots

print(JobScheduling([("A",2,100),("B",1,19),("C",2,27),("D",1,25),("E",3,15)],3))
