import sys
import math

T = int(input())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y-x
    n = int(math.sqrt(distance))
    time = 2*n - 1
    distance -= n**2
    
    while distance > 0:
        distance -= n
        time += 1
    
    print(time)