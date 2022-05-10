import sys
sys.setrecursionlimit(1000000)

def find_time(building):
    if building in orders:
        for pre_building in orders[building]:
            if pre_building not in visited:
                find_time(pre_building)
                visited.add(pre_building)
        Time[building] += max(Time[pre] for pre in orders[building])

T = int(sys.stdin.readline())
for test in range(T):
    N, K = map(int, sys.stdin.readline().split())
    Time = [0] + list(map(int, sys.stdin.readline().split()))
    orders = {}
    for order in range(K):
        A, B = map(int, sys.stdin.readline().split())
        orders[B] = orders.get(B, []) + [A]
    W = int(sys.stdin.readline())
    visited = set([])
    find_time(W)
    print(Time[W])