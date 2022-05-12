import sys

def crossv(x, y):
    return(x[0]*y[1]-x[1]*y[0])

N = int(input())

x0, y0 = map(int, sys.stdin.readline().split())
before = [x0, y0]
S = 0

for i in range(N - 1):
    after = list(map(int, sys.stdin.readline().split()))
    S += crossv(before, after)
    before = after

after = [x0, y0]
S += crossv(before, after)

print(abs(S/2))