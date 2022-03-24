# 1920
import sys

N = int(sys.stdin.readline())
num_list = set(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))

for find in find_list:
    if find in num_list:
        print(1)
    else:
        print(0)

# 10816
import sys

N = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_set = set(num_list)
dic = {}

for find in find_list:
    if find in num_set:
        dic[find] = dic.get(find, 0) + 1

for num in num_list[:-1]:
    print(dic.get(num, 0), end=' ')
print(dic.get(num_list[-1], 0))

# 1654
import sys

N, K = map(int, sys.stdin.readline().split())
num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

a, b = 1, max(num_list)+1
while b - a > 1:
    num = 0
    c = (b + a)//2 
    for i in num_list:
        num += (i//c)
    if num >= K:
        a = c
    else:
        b = c
print(a)

# 2805
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

a, b = 0, max(num_list)
while b - a > 1:
    num = 0
    c = (b + a)//2 
    for i in num_list:
        num += max(i-c, 0)
    if num >= M:
        a = c
    else:
        b = c
print(a)

# 2110


# 1300


# 12015
