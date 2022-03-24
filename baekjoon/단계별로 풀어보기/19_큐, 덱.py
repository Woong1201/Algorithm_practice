# 8258
from collections import deque
import sys

N = int(input())
que = deque()

for i in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        que.append(order[1])
    elif order[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

# 2164
from collections import deque

que = deque([i for i in range(1, int(input())+1)])

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])

# 11866
import sys

N, K = map(int, sys.stdin.readline().split())
circle = [i for i in range(1, N+1)]

index = K - 1
print('<{}'.format(circle.pop(index)), end='')
while len(circle):
    index = (index + K - 1)%len(circle)
    print(', {}'.format(circle.pop(index)), end='')
print('>')

# 1966
from collections import deque
import sys

test = int(sys.stdin.readline())
for i in range(test):
    N, M = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))
    num_sort = deque(sorted(num_list, key=lambda x:-x))
    count = 1
    index = 0
    num = num_sort.popleft()
    while len(num_sort):
        if num_list[index] == num:
            if index == M:
                break
            count += 1
            num = num_sort.popleft()
        index = (index + 1)%len(num_list)
    print(count)

# 10866
from collections import deque
import sys

N = int(input())
que = deque()

for i in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        que.appendleft(order[1])
    elif order[0] == 'push_back':
        que.append(order[1])
    elif order[0] == 'pop_front':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif order[0] == 'pop_back':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop())
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

# 1021
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
num_que = deque(i for i in range(1, N+1))
to_do = deque(map(int, sys.stdin.readline().split()))
count = 0

while len(to_do):
    do = to_do.popleft()
    if num_que.index(do) <= len(num_que)-num_que.index(do):
        while num_que[0]!=do:
            num_que.append(num_que.popleft())
            count+=1
    else:
        while num_que[0]!=do:
            num_que.appendleft(num_que.pop())
            count+=1

    num_que.popleft()

print(count)

# 5430
from collections import deque
import sys

T = int(input())
for i in range(T):
    function = sys.stdin.readline().rstrip()
    n = int(input())
    num_list = deque(sys.stdin.readline()[1:-2].split(','))
    if n == 0:
        num_list = deque([])
    eroor = 0
    reverse = 1
    for f in function:
        if f == 'R':
            reverse *= -1
        elif len(num_list) == 0:
            print('error')
            eroor = 1
            break
        elif reverse == 1:
            num_list.popleft()
        else:
            num_list.pop()
    if eroor == 0:
        if reverse == -1:
            num_list.reverse()
        print('[{}]'.format(','.join(num_list)))