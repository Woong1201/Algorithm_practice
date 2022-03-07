import sys
import math

def power(a, n):
    if n == 0:
        return 1
    x = power(a, n//2)
    if n%2 == 0:
        return x**2%1000000007
    else :
        return x**2*a%1000000007

N = int(input())
expectation = [0, 1]

for i in range(N):
    prob = list(map(int, sys.stdin.readline().split()))
    expectation = [expectation[0]*prob[0]+expectation[1]*prob[1], expectation[1]*prob[0]]

gcd = math.gcd(expectation[0],expectation[1])
expectation = [expectation[0]//gcd, expectation[1]//gcd]

print(((expectation[0]%1000000007)*(power(expectation[1],1000000005)%1000000007))%1000000007)