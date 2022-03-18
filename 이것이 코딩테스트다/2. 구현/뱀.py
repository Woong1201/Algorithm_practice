from collections import deque
import sys

def rotate(direction, r):
    if r == 0:
        return direction
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    if r == 'D':
        return directions[(directions.index(direction)+1)%4]
    return directions[(directions.index(direction)-1)]

N = int(input())
K = int(input())
apple = [list(map(int,sys.stdin.readline().split())) for i in range(K)]
R = int(input())
rotation = {}
for i in range(R):
    rot = list(sys.stdin.readline().split())
    rotation[int(rot[0])] = rot[1]

snake = deque([[1,1]])
direction = [0,1]
time = 0
while True:
    time += 1
    location = [snake[-1][0]+direction[0],snake[-1][1]+direction[1]]
    
    if location[0] < 1 or location[0] > N or location[1] < 1 or location[1] > N or location in snake:
        print(time)
        break
    
    if location in apple:
        apple.remove(location)
    else:
        snake.popleft()
    
    snake.append(location)
    direction = rotate(direction, rotation.get(time, 0))