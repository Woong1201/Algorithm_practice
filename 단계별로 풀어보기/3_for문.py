# 2739
a = int(input())
for i in range(1, 10):
    print(a, '*', i, '=', a*i)

# 10950
a = int(input())
for i in range(a):
    b, c = input().split()
    print(int(b) + int(c))

# 8293
a = int(input())
answer = a
for i in range(a):
    answer += i
print(answer)

# 15552
import sys
a = int(input())
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    print(b+c)

# 2741
a = int(input())
for i in range(a):
    print(i + 1)

# 2742
a = int(input())
for i in range(a):
    print(a - i)

# 11021
import sys
a = int(input())
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1}".format(i+1, b+c)) 

# 11022
import sys
a = int(input())
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, b, c, b+c)) 

# 2438
a = int(input())
for i in range(a):
    print("*"*(i+1))

# 2439
a = int(input())
for i in range(a):
    print(" "*(a-1-i) + "*"*(i+1))

# 10871
import sys
N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = []
for i in range(N):
    if A[i] < X:
        answer.append(str(A[i]))
print(' '.join(answer))