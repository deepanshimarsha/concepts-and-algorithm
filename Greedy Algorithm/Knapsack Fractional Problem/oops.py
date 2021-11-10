class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def knapsack(n,arr,capaity):
    obj = []
    for i in range(n):
        obj.append(Item(arr[i][0],arr[i][1]))

    max_profit = 0
    curr_weight = 0
    for items in sorted(obj, key=lambda x: x.ratio, reverse=True):
        print(items.weight)
        curr_weight += items.weight
        if curr_weight <= capaity:
            max_profit += items.profit
        else:
            print(max_profit)
            #print(items.ratio)
            max_profit += items.ratio*(items.weight-(curr_weight-capaity))
            break
    return max_profit

print(knapsack(7,[(2,10),(3,5),(5,15),(7,7),(1,6),(4,18),(1,3)],15))