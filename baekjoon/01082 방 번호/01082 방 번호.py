import sys

N = int(input())
prices = list(map(int, sys.stdin.readline().split()))
prices = [(prices[i],-i) for i in range(N)]
money = int(input())

if N == 1 or min(prices[1:])[0] > money:
    print(0)

else:
    min_val1 = min(prices[1:])
    answer = str(-min_val1[1])
    money -= min_val1[0]

    min_val = min(prices)
    while min_val[0] <= money:
        money -= min_val[0]
        answer += str(-min_val[1])

    prices.sort(key=lambda x:x[1])
    for price in prices:
        if min_val1[0] + money >= price[0] and -min_val1[1] < -price[1]:
            answer = str(-price[1]) + answer[1:]
            money -= (price[0] - min_val1[0])
            break
            
    idx = 1
    while True:
        for price in prices:
            if min_val[0] + money >= price[0] and -min_val[1] < -price[1]:
                answer = answer[:idx] + str(-price[1]) + answer[idx+1:]
                money -= (price[0] - min_val[0])
                idx += 1
                break
        else:
            break                
    
    print(answer)