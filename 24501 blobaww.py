import sys

N, M = map(int, sys.stdin.readline().split())
dic_E, dic_S, answer = {i:0 for i in range(M)}, {i:0 for i in range(M)}, 0

for i in range(N):
    line = sys.stdin.readline()
    x = 0
    y = 0
    for j in range(M):
        if line[j] == 'E':
            x += 1
            dic_E[j] += x
            dic_S[j] += y
        elif line[j] == 'S':
            dic_E[j] += x
            y += dic_E[j]
            dic_S[j] += y 
        else :
            dic_E[j] += x
            dic_S[j] += y
            answer += dic_S[j]

print(answer%(10**9 + 7))