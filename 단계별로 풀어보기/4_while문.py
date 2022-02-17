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

# 1110
a = int(input())
b = (a%10)*10 + (a//10 + a%10)%10
t = 1
while a!=b:
    b = (b%10)*10 + (b//10 + b%10)%10
    t+=1
print(t)