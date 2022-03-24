# 2798
import sys
a, b = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1,a):
            if answer < num[i]+num[j]+num[k] <= b:
                answer = num[i]+num[j]+num[k]
print(answer)

# 2231
p = 1
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if 100001*i + 10001*j + 1001*k + 101*l + 11*m + 2*n == a:
                            print(100001*i + 10001*j + 1001*k + 101*l + 11*m + 2*n)
                            p = 0
                            break
                    if p == 0:
                        break
                if p == 0:
                    break
            if p == 0:
                break
        if p == 0:
            break
    if p == 0:
        break
if p==1:
    print(0)

# 7568
import sys
a = int(input())
lines = sys.stdin.readlines()
answer = [1]*a
for i in range(a-1):
    x1, y1 = map(int, lines[i].split())
    for j in range(i+1, a):
        x2, y2 = map(int, lines[j].split())
        if x1 > x2 and y1 > y2:
            answer[j] += 1
        elif x1 < x2 and y1 < y2:
            answer[i] += 1
    print(answer[i])
print(answer[-1])

# 1018
import sys
M, N = map(int, sys.stdin.readline().split())
lines = sys.stdin.readlines()
answer = []
for p in range(0, M-7):
    for q in range(0, N-7):
        ans = 0
        for i in range(p, p+8):
            for j in range(q, q+8):
                if (i+j)%2 == 0 and lines[i][j] == 'B':
                    ans += 1
                if (i+j)%2 == 1 and lines[i][j] == 'W':
                    ans += 1
        answer.append(min(ans, 64-ans))
print(min(answer))
         
# 1436
a = int(input())
b = 665
while a:
    b += 1
    if '666' in str(b):
        a-=1
print(b)