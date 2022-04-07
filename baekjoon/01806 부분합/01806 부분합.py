import sys

N, S = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))
start, end, array_len, sum_array = 0, 0, 0, 0
num_len = N + 1

while num_len - 1:
    if array_len > num_len:
        sum_array -= array[start]
        start += 1
        array_len -= 1
        continue
    
    if sum_array >= S:
        num_len = min(array_len, num_len)
        sum_array -= array[start]
        start += 1
        array_len -= 1
    elif end == N:
        break 
    else:
        sum_array += array[end]
        end += 1
        array_len += 1

if num_len == N + 1:
    print(0)
else:
    print(num_len)