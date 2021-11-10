def FractionalKnapsack(n,profit,weight,capacity):
    ratio = {}
    for i in range(n):
        ratio[i] = profit[i] / weight[i]

    #print(ratio)
    #print(sorted(ratio.values()))
    sum = 0
    max_profit = 0
    seen = set()

    for value in sorted(ratio.values(),reverse=True):

        idx = getkey(ratio,value,seen)
        seen.add(idx)
        #print(idx)
        
        sum += weight[idx]
        max_profit += profit[idx]
        if sum == capacity:
            break
        elif sum > capacity:
            weight = sum - capacity
            print(weight, weight*value)
            max_profit = max_profit - weight*value
            break
        

    return max_profit

def getkey(dic, value, seen):
    for key in dic:
        if dic[key] == value and key not in seen:
            return key
    
print(FractionalKnapsack(7,[10,5,15,7,6,18,3],[2,3,5,7,1,4,1],15))