# 10818, 2562, 2577, 3052, 1546, 8958, 4344
import sys
a = int(input())
b = list(map(int, sys.stdin.readline().split()))
print(min(b), max(b))

# 2562
import sys
lines = sys.stdin.readlines()
a = 0
b = 0
for i in range(9):
    if int(lines[i])>a:
        a = int(lines[i])
        b = i+1
print(a)
print(b)

# 2577
import sys
lines = sys.stdin.readlines()
a, b, c = int(lines[0]), int(lines[1]), int(lines[2])
answer = str(a*b*c)
for i in range(10):
    p = 0
    for j in range(len(answer)):
        if answer[j] == str(i):
            p += 1
    print(p)

# 3052
x = set()
for i in range(10):
    x.add(int(input())%42)
print(len(x))

# 1546
import sys
a = int(input())
b = list(map(int, sys.stdin.readline().split()))
print(sum(b)/a*100/max(b))

# 8958
import sys
a = int(input())
for i in range(a):
    b = sys.stdin.readline()
    point = 0
    c = 0
    for j in range(len(b[:-1])):
        if b[j] == 'X':
            c = 0
        else:
            c += 1
        point += c
    print(point)

# 4344
import sys
a = int(input())
for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    c = 0
    mean = sum(b[1:])/b[0]
    for j in b[1:]:
        if j > mean:
            c += 1
    rate = c/b[0]*100
    print("%.3f%%" %round(rate, 3))