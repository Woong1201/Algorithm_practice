# 2750
from statistics import median
import sys
a = int(input())
answer = []
for i in range(a):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in range(a):
    print(answer[i])

# 2751
import sys
a = int(input())
answer = []
for i in range(a):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in range(a):
    print(answer[i])

# 10989
import sys
a = int(input())
counting_array = [0]*10001
for i in range(a):
    b = int(sys.stdin.readline())
    counting_array[b] += 1
p = 0
while a:
    for i in range(counting_array[p]):
        print(p)
        a-=1
    p+=1

# 2108
import sys
import math
def real_round(x):
    print(round(x-math.trunc(x)+1)+math.trunc(x)-1)
a = int(input())
counting_array = [0]*8001
sumn = 0
mx, mn = -4000, 4000
for i in range(a):
    b = int(sys.stdin.readline())
    counting_array[b + 4000] += 1
    if b > mx:
        mx = b
    if b < mn:
        mn = b
    sumn += b

p, q = 0, [0, 0]
r = [0, 0, 0]
for i in range(8001):
    c = counting_array[i]
    p += c
    if q[0]==0 and p >= (a+1)//2:
        q = [1, i-4000]
    if r[0] < c:
        r = [c,0,i-4000]
    elif r[0] == c and r[1]==0:
        r = [c,1,i-4000]
    if p == a:
        break
real_round(sumn/a)
print(q[1])
print(r[2])
print(mx-mn)

# 1427
a = int(input())
answer = []
while a:
    answer.append(a%10)
    a = a//10
answer = sorted(answer, key=lambda x: -x)
for i in answer:
    print(i)

# 11650
import sys
a = int(input())
answer = [list(map(int, sys.stdin.readline().split())) for i in range(a)]
for i in sorted(answer):
    print('{0} {1}'.format(i[0], i[1]))

# 11651
import sys
a = int(input())
answer = [list(map(int, sys.stdin.readline().split())) for i in range(a)]
for i in sorted(answer, key = lambda x: (x[1], x[0])):
    print('{0} {1}'.format(i[0], i[1]))

# 1181
import sys
a = int(input())
answer = list(set(sys.stdin.readline()[:-1] for i in range(a)))
for i in sorted(answer, key = lambda x: (len(x),x)):    
    print(i)

# 10814
import sys
a = int(input())
answer = [list(sys.stdin.readline().split()) for i in range(a)]
for i in sorted(answer, key = lambda x: int(x[0])):
    print('{0} {1}'.format(i[0], i[1]))

# 18870
import sys
a = int(input())
xn = list(map(int, sys.stdin.readline().split()))
xn_ = sorted(set(xn))
dic = {}
for i, j in enumerate(xn_):
    dic[j] = i
for i in xn[:-1]:
    print(dic[i], end=' ')
print (dic[xn[-1]])