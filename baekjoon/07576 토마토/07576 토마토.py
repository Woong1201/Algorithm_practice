from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
unripe = set()
ripe = set()

for row in range(N):
    for col, tomato in enumerate(list(map(int, sys.stdin.readline().split()))):
        if tomato == 0:
            unripe.add((row, col))
        elif tomato == 1:
            ripe.add((row, col))

moves = [[0,1],[1,0],[-1,0],[0,-1]]
time = 0

while ripe and unripe:
    new_ripe = set()
    for tomato in ripe:
        for move in moves:
            if (tomato[0]+move[0], tomato[1]+move[1]) in unripe:
                new_ripe.add((tomato[0]+move[0], tomato[1]+move[1]))
                unripe.remove((tomato[0]+move[0], tomato[1]+move[1]))
    time += 1
    ripe = new_ripe

if len(unripe) == 0:
    print(time)
else:
    print(-1)