from bisect import bisect_left
import sys

def choice_wifi(x):
    indexs = [0]
    index = 0
    for i in range(C-1):
        index = bisect_left(houses, houses[index] + x)
        if index >= N:
            return False
        indexs.append(index)
    return True


N, C = map(int, sys.stdin.readline().split())
houses = sorted(int(sys.stdin.readline()) for i in range(N))

start, end = 1, 1000000001

while start+1 < end:
    mid = (end + start) // 2
    if choice_wifi(mid):
        start = mid
    else:
        end = mid
        
print(start)


# bisect함수 공부