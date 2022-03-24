import sys

N = int(input())
num_list = list(map(int,sys.stdin.readline().split()))
LIS = {0:0}
LDS = {0:0}
answer = [0]*N

for num in range(N):
    for i in LIS:
        if LIS[i] < num_list[num]:
            p = i
    if LIS.get(p+1, 1001) > num_list[num]:
        LIS[p+1] = num_list[num]

    for i in LDS:
        if LDS[i] < num_list[N-num-1]:
            q = i
    if LDS.get(q+1, 1001) > num_list[N-num-1]:
        LDS[q+1] = num_list[N-num-1]
    
    answer[num] += p+1
    answer[N-num-1] += q

print(max(answer))