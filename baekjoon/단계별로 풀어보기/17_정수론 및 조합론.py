# 5086
import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    if A % B == 0:
        print('multiple')
    elif B % A == 0:
        print('factor')
    else:
        print('neither')

# 1037
import sys

N = int(input())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

print(num_list[0]*num_list[-1])

# 2609
import sys

A, B =map(int, sys.stdin.readline().split())

for i in range(1, min(A,B)+1):
    if A%i == 0 and B%i == 0:
        gcd = i

print(gcd)
print(A*B//gcd)

# 1934
import sys

N = int(input())

for i in range(N):
    A, B =map(int, sys.stdin.readline().split())
    
    for i in range(1, min(A,B)+1):
        if A%i == 0 and B%i == 0:
            gcd = i

    print(A*B//gcd)

# 2981
import sys
import math

def get_divisor(x):
    divisor = []
    num = 2
    while num < math.sqrt(x):
        if x%num == 0:
            divisor.append(num)
            divisor.append(x//num)
        num += 1
    if x%(num) == 0 and num not in divisor:
        divisor.append(num)
    return (sorted(divisor))

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

gcd = abs(num_list[-1] - num_list[0])
for i in range(1, N):
    gcd = math.gcd(gcd, abs(num_list[i]-num_list[i-1]))

if gcd == 2:
    print(gcd)
else:
    for i in get_divisor(gcd):
        print(i, end=' ')
    print(gcd)

# 3036
import sys
import math

N = int(input())
ring_list = list(map(int, sys.stdin.readline().split()))
ring = ring_list[0]

for ring2 in ring_list[1:]:
    gcd = math.gcd(ring, ring2)
    print('{0}/{1}'.format(ring//gcd,ring2//gcd))

# 11050
import sys
import math

N, K = map(int, sys.stdin.readline().split())
print(math.comb(N,K))

# 11051
import sys
import math

N, K = map(int, sys.stdin.readline().split())
print(math.comb(N,K)%10007)

# 1010
import sys
import math

for i in range(int(input())):
    N, M = map(int, sys.stdin.readline().split())
    print(math.comb(M,N))

# 9375
import sys
import math

for i in range(int(input())):
    clothes = {}
    for j in range(int(sys.stdin.readline())):
        N, M = sys.stdin.readline().split()
        if clothes.get(M, 0) == 0:
            clothes[M] = 1
        clothes[M]+=1
    answer = 1
    for num in clothes.values():
        answer *= num
    print(answer-1)

# 1676
import sys
import math

N = math.factorial(int(input()))
answer = 0
while True:
    if N % 10 != 0: 
        break
    N = N//10
    answer+=1
print(answer)

# 2004
import sys
import math

def num_25(x,i):
    num = 0
    while x>0:
        num += x//i
        x = x//i
    return num

N, M = map(int, sys.stdin.readline().split())
print(min(num_25(N,5)-num_25(M,5)-num_25(N-M,5),num_25(N,2)-num_25(M,2)-num_25(N-M,2)))