# 1003
import sys
dic = {0 : [1,0], 1:[0,1]}
def fibonacci(x):
    if x not in dic:
        fibonacci(x-1)
        dic[x] = [dic[x-1][0] + dic[x-2][0], dic[x-1][1]+dic[x-2][1]]

a = int(input())
for i in range(a):
    x=(int(sys.stdin.readline()))
    fibonacci(x)
    print(dic[x][0], dic[x][1])

# 9184
import sys

def w(a,b,c):
    if (a,b,c) in dic:
        return
    elif a <= 0 or b <= 0 or c <= 0:
        dic[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        w(20, 20, 20)
        dic[(a, b, c)] = dic[(20, 20, 20)]
    elif a < b and b < c:
        w(a, b, c-1)
        w(a, b-1, c-1)
        w(a, b-1, c)
        dic[(a, b, c)] = dic[(a, b, c-1)] + dic[(a, b-1, c-1)] - dic[(a, b-1, c)]
    else:
        w(a-1, b, c)
        w(a-1, b-1, c)
        w(a-1, b, c-1)
        w(a-1, b-1, c-1)
        dic[(a, b, c)] = dic[(a-1, b, c)] + dic[(a-1, b-1, c)] + dic[(a-1, b, c-1)] - dic[(a-1, b-1, c-1)]

dic = {}
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    w(a,b,c)
    print('w({0}, {1}, {2}) ='.format(a,b,c), dic[(a,b,c)])

# 1904
def tile(x):
    if x not in dic:
        dic[x] = (dic[x-1]+dic[x-2])%15746

dic = {1:1, 2:2}
a = int(input())
for i in range(1,a+1):
    tile(i)
print(dic[a])

# 9461
import sys
def triangle(x):
    if x not in dic:
        triangle(x-1)
        dic[x] = dic[x-1]+dic[x-5]

dic = {1:1, 2:1, 3:1, 4:2, 5:2}
a = int(input())
for i in range(a):
    N = int(sys.stdin.readline())
    triangle(N)
    print(dic[N])

# 1149
import sys
N = int(input())
val = [0,0,0]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    new_val = []
    new_val.append(min(val[1],val[2])+line[0])
    new_val.append(min(val[0],val[2])+line[1])
    new_val.append(min(val[0],val[1])+line[2])
    val = new_val

print(min(val))

# 1932
import sys
N = int(input())
val = [int(input())]

for i in range(1, N):
    line = list(map(int, sys.stdin.readline().split()))
    new_val = []
    new_val.append(val[0]+line[0])
    for j in range(1, i):
        new_val.append(max(val[j-1],val[j])+line[j])
    new_val.append(val[-1]+line[-1])
    val = new_val

print(max(val))

# 2579
import sys

N = int(input())
stair = {-1:[0,0], 0:[0,0]}

for i in range(1, N+1):
    val = int(sys.stdin.readline())
    stair[i] = [max(stair[i-2])+val, stair[i-1][0]+val]

print(max(stair[N]))

# 1463
dic = {1:0}
def make1(x):
    if x not in dic:
        make1(x-1)
        if x%6 == 0:
            make1(x//3)
            make1(x//2)
            dic[x] = min(dic[x-1],dic[x//3],dic[x//2]) + 1
        elif x%3 == 0:
            make1(x//3)
            dic[x] = min(dic[x-1],dic[x//3]) + 1
        elif x%2 == 0:
            make1(x//2)
            dic[x] = min(dic[x-1],dic[x//2]) + 1
        else:
            dic[x] = dic[x-1] + 1
N = int(input())
for i in range(1,N+1):
    make1(i)
print(dic[N])

# 10844
N = int(input())
num = {i:1 for i in range(-1,11)}
num[0], num[-1], num[10] = 0, 0, 0

for i in range(N-1):
    num = {j:num[j-1]+num[j+1] for j in range(10)}
    num[-1], num[10] = 0, 0

print((sum(list(num.values())))%1000000000)

# 2156
import sys

N = int(input())
wine = {-2:[0,0], -1:[0,0], 0:[0,0]}

for i in range(1, N+1):
    val = int(sys.stdin.readline())
    wine[i] = [max(wine[i-2]+wine[i-3])+val, wine[i-1][0]+val]

print(max(wine[N]+wine[N-1]))

# 11053
import sys

N = int(input())
num_list = list(map(int,sys.stdin.readline().split()))
LIS = {0:0}

for num in num_list:
    p = 0
    for i in LIS:
        if LIS[i] < num:
            p = i
    if LIS.get(p+1, 1001) > num:
        LIS[p+1] = num

print(max(list(LIS.keys())))

# 11054
import sys

N = int(input())
num_list = list(map(int,sys.stdin.readline().split()))
LIS = {0:0}
LDS = {0:0}
answer = [0]*N

for num in range(N):
    for i in LIS:
        if LIS[i] < num_list[num]:
            p = i
    if LIS.get(p+1, 1001) > num_list[num]:
        LIS[p+1] = num_list[num]

    for i in LDS:
        if LDS[i] < num_list[N-num-1]:
            q = i
    if LDS.get(q+1, 1001) > num_list[N-num-1]:
        LDS[q+1] = num_list[N-num-1]
    
    answer[num] += p+1
    answer[N-num-1] += q

print(max(answer))

# 2565
import sys

N = int(input())
num_list = sorted([list(map(int,sys.stdin.readline().split())) for i in range(N)])
LIS = {0:0}

for num in num_list:
    p = 0
    for i in LIS:
        if LIS[i] < num[1]:
            p = i
    if LIS.get(p+1, 1001) > num[1]:
        LIS[p+1] = num[1]

print(N - max(list(LIS.keys())))

# 9251


# 1912


# 12865