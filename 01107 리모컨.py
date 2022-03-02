import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
button = list(sys.stdin.readline().split())

time = abs(N - 100)
index = 0
possible = 0

while (time - index)!=0:
    next_channel = str(N + index)
    before_channel = str(N - index)
    for i in next_channel:
        if i in button:
            break
    else:
        possible = 1
    if N >= index:
        for i in before_channel:
            if i in button:
                break
        else:
            possible = 2
    if possible!=0:
        break
    index += 1

if possible == 0:
    print(time)
elif possible == 1:
    print(min(time, index+len(next_channel)))
else:
    print(min(time, index+len(before_channel)))