import sys
sys.setrecursionlimit(100000)

def Tree(x, y):
    for i in range(len(info[x])//2):
        if info[x][i*2] == y:
            pass
        else:
            Tree(info[x][i*2],x)
    max1 = [0, 0]
    info_x = info.pop(x)
    for i in range(len(info_x)//2):
        if info_x[2*i] == y:
            pass
        else:
            # p = distance[info_x[2*i]] + info_x[2*i+1]
            p = distance.pop(info_x[2*i]) + info_x[2*i+1]
            if p > max1[0]:
                max1[1] = max1[0]
                max1[0] = p
            elif p > max1[1]:
                max1[1] = p
    if sum(max1) > max[0]:
        max[0] = sum(max1)
    distance[x] = max1[0]

N = int(input())
info = {}
max = [0]
distance = {}

for i in range(1, N+1):
    info[i] = list(map(int, sys.stdin.readline().split()))[1:-1]

Tree(1,0)
print(max[0])

# print(info)
# Tree(1,0)
# print(distance)
# print(max[0])

# 12
# 1 2 3 3 2 -1
# 2 1 3 4 5 -1
# 3 1 2 5 11 6 9 -1
# 4 2 5 7 1 8 7 -1
# 5 9 15 3 11 10 4 -1
# 6 3 9 11 6 12 10 -1
# 7 4 1 -1
# 8 4 7 -1
# 9 5 15 -1
# 10 5 4 -1
# 11 6 6 -1
# 12 6 10 -1