import sys

N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
num_M = 0

while start < N:
    sum_array = sum(array[start: end])
    if sum_array == M:
        num_M += 1

    if sum_array > M or end == N:
        start += 1
    elif sum_array <= M:
        end += 1
    
print(num_M)