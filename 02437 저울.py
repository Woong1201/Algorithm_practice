import sys

N = int(input())
num_list = sorted(map(int, sys.stdin.readline().split()))

target = 1
for num in num_list:
    if target >= num:
        target += num
    else:
        break
print(target)