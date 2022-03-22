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