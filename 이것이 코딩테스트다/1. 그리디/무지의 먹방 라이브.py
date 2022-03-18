def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    first = 0
    length = len(food_times)
    max = k//length
    while True:    
        rest = []
        
        if first == 0:
            for index, food in enumerate(food_times):
                if food <= max:
                    k -= food
                else:
                    k -= max
                    rest.append((food - max, index+1))
            first = 1
            food_times = sorted(rest)
        else:
            for food in food_times:
                if food[0] <= max:
                    k -= food[0]
                else:
                    k -= max
                    rest.append((food[0]-max,food[1]))
            food_times = rest
        
        length = len(food_times)
        max = k//length
        if food_times[0][0]*length >= k:
            return sorted(food_times, key = lambda x : x[1])[k%length][1]
        

food_times = [3,1,2]
k = 5
print(solution(food_times, k))