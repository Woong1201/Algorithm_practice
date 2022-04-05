import sys

N = int(input())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

min_val = abs(sum(num_list[:3]))
min_list = num_list[:3]

for i, num in enumerate(num_list):
    start = 0
    end = N-1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        val = num_list[start] + num_list[end] + num
        if abs(val) < min_val:
            min_val, min_list = abs(val), [num_list[start], num_list[end], num]
        if val < 0:
            start += 1    
        else:
            end -= 1
          
    if val == 0:
        break

min_list.sort()
print(min_list[0], min_list[1], min_list[2])