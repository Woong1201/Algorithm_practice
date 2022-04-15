from collections import deque

n, k = map(int, input().split())

if n > k:
    print(0)
else:
    lift = 0
    dramatic_num = deque([str(k)])
    num = k
    while True:
        new_num = num*n + lift
        if new_num == k:
            break
        num, lift = (new_num)%10, (new_num)//10
        dramatic_num.appendleft(str(num))

    print(''.join(dramatic_num))