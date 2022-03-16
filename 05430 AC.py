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