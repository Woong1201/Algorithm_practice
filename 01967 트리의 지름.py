import sys
sys.setrecursionlimit(100000)

def Tree(x):
    for i in range(len(info[x])//2):
        Tree(info[x][i*2])
    max1 = [0, 0]
    info_x = info.pop(x)
    for i in range(len(info_x)//2):
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
info = {i:[] for i in range(1,N+1)}
max = [0]
distance = {}

for i in range(N-1):
    j = list(map(int, sys.stdin.readline().split()))
    info[j[0]] += j[1:]

Tree(1)
print(max[0])