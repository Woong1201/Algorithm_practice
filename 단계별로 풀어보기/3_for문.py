# 2739, 10950, 8293, 15552, 2741, 2742, 11021, 11022
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

Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7