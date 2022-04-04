import sys

N = int(input())
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

if N == 1:
    print(a+b+c+d+e+f-max(a,b,c,d,e,f))
else:
    num1 = min(a,b,c,d,e,f)
    num2 = min(a+b, a+c, a+d, a+e, f+b, f+c, f+d, f+e, b+d, d+e, e+c, c+b)
    num3 = min(a+c+b, a+b+d, a+d+e, a+e+c, f+c+b, f+b+d, f+d+e, f+e+c)
    print(num1*(5*(N-2)**2+4*(N-2))+num2*(8*(N-2)+4)+num3*4)