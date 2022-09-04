import heapq
import sys

# 노드수, 간선수, 한점
N, M, X = map(int, sys.stdin.readline().split())
connects = {}
# 간선 입력
for _ in range(M):
    a, b, time = map(int, sys.stdin.readline().split())
    if a not in connects:
        connects[a] = []
    connects[a].append([b, time])

# X에서 출발하여 각 노드로 가는 거리 계산 (다익스트라 알고리즘)
from_x = [1000001]*(N+1)
from_x[X] = 0
locations = [[0, X]]
while locations:
    time, loc = heapq.heappop(locations)
    if from_x[loc] != time:
        continue

    for new_loc, new_time in connects[loc]:
        if from_x[new_loc] > time+new_time:
            from_x[new_loc] = time+new_time
            heapq.heappush(locations, [time+new_time, new_loc])

# 각 노드에서 출발하여 X로 가는 거리 계산
ans = 0
for node in range(1, N+1):
    dp = [1000001]*(N+1)
    dp[node] = 0
    locations = [[0, node]]
    while True:
        time, loc = heapq.heappop(locations)
        if dp[loc] != time:
            continue
        if loc == X:
            break

        for new_loc, new_time in connects[loc]:
            if dp[new_loc] > time+new_time:
                dp[new_loc] = time+new_time
                heapq.heappush(locations, [time+new_time, new_loc])

    # 계산 완료시 ans 갱신
    new_ans = from_x[node] + time
    if ans < new_ans:
        ans = new_ans

print(ans)