import sys

N = int(input())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

new_sort = [num_list[0]]
idx = -1 #idx_blank
for num in num_list[1:]:
    if idx != -1 and num != new_sort[idx-1]+1:
        new_sort[idx] = num
        idx = -1
        continue

    if num != new_sort[-1]+1:
        new_sort.append(num)
    else:
        idx = len(new_sort)
        new_sort += [-1, num]

if idx != -1:
    num1, idx_num1 = new_sort[idx-1], idx
    while idx_num1 > 0:
        if new_sort[idx_num1-1] != num1:
            break
        idx_num1 -= 1
    new_sort = new_sort[:idx_num1] + new_sort[idx+1:] + new_sort[idx_num1:idx]

for num in new_sort[:-1]:
    print(num, end=' ')
print(new_sort[-1])