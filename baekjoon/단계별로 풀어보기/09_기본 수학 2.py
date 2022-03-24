# 1978
import sys
import math
def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
a = int(input())
b = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in b:
    if isprime(i):
        answer += 1
print(answer)

# 2581
import sys
import math
def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
a = int(input())
b = int(input())
answer = []
for i in range(a, b + 1):
    if isprime(i):
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    print (sum(answer))
    print (answer[0])

# 11653
a = int(input())
while a>=2:
    for i in range(2, a+1):
        if a%i==0:
            print(i)
            a = a//i
            break

# 1929
import sys
import math
def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
a, b = map(int, sys.stdin.readline().split())
for i in range(a, b + 1):
    if isprime(i):
        print(i)

# 4948
import sys
import math
def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
dic = {}
answer = 0
for i in range(1, 123456*2 + 1):
    if isprime(i):
        answer += 1
    dic[i] = answer
a = int(sys.stdin.readline())
while a:
    print(dic[2*a]-dic[a])
    a = int(sys.stdin.readline())

# 9020
import math
def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
a = int(input())
for i in range(a):
    b = int(input())
    c = b//2
    while True:
        if isprime(c) and isprime(b-c):
            break
        c -= 1
    print (c, b-c)

# 1085
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, w-x, h-y))

# 3009
import sys
x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())
if x1 == x2:
    x = x3
elif x2 == x3:
    x = x1
else :
    x = x2
if y1 == y2:
    y = y3
elif y2 == y3:
    y = y1
else :
    y = y2
print (x, y)

# 4153
import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        break
    C = max(a, b, c)
    A = min(a, b, c)
    B = a + b + c - A - C
    if C**2 == A**2 + B**2:
        print("right")
    else :
        print('wrong')

# 3053
import math
a = int(input())
print (a*a*math.pi)
print (a*a*2)

# 1002
import sys
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y1-y2)**2)
a = int(input())
for i in range(a):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:    
        if distance(x1, y1, x2, y2) > r1+r2 or distance(x1, y1, x2, y2) < abs(r2-r1):
            print(0)
        elif distance(x1, y1, x2, y2) == r1+r2 or distance(x1, y1, x2, y2) == abs(r2-r1):
            print(1)
        elif abs(r2-r1) < distance(x1, y1, x2, y2) < r1+r2:
            print(2)