# 10952
import sys
a, b = map(int, input().split())
while a:
    print (a + b)
    a, b = map(int, input().split())

# 10951
import sys
lines = sys.stdin.readlines()
for line in lines:
    a, b  = map(int, line.split())
    print(a+b)