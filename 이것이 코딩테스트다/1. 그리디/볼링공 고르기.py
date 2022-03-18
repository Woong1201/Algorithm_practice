import sys
import math

N, M = map(int, sys.stdin.readline().split())
bowls = list(map(int, sys.stdin.readline().split()))

answer = math.comb(N,2)
for i in range(1, M+1):
    answer -= math.comb(bowls.count(i),2)

print(answer)