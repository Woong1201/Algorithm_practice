# 1712
import sys
import math
from tkinter import X
a, b, c = map(int, sys.stdin.readline().split())
if b >= c:
    print(-1)
else :
    print(math.trunc(a//(c-b)+1))

# 2292
import math
a = (int(input()) + 4)//6
b = math.trunc(math.sqrt(2*a))
if a <= b*(b+1)/2:
    print(b+1)
else :
    print(b+2)

# 1193
import math
a = int(input())
b = math.trunc(math.sqrt(2*a))
if a > b*(b+1)/2:
    b+=1
x = a - b*(b-1)//2
y = b - x + 1
if b%2 == 0:
    print("{0}/{1}".format(x, y))
else:
    print("{0}/{1}".format(y, x))

# 2869
import sys
import math
a, b, c = map(int, sys.stdin.readline().split())
print(math.ceil((c-a)/(a-b))+1)

# 10250
import sys
a = int(input())
for i in range(a):
    H, W, N = map(int, sys.stdin.readline().split())
    x, y = str(N % H), '0' + str((N-1)//H + 1)
    if x == '0':
        x = str(H)
    print(x+y[-2:])

# 2775
import math
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(math.factorial(n+k)//math.factorial(n-1)//math.factorial(k+1))

# 2839
a = int(input())
if a in [4, 7]:
    print(-1)
elif a%5 == 0:
    print(a//5)
elif a%5 == 1:
    print(a//5+1)
elif a%5 == 2:
    print(a//5+2)
elif a%5 == 3:
    print(a//5+1)
elif a%5 == 4:
    print(a//5+2)

# 10757
print(sum(map(int, input().split())))