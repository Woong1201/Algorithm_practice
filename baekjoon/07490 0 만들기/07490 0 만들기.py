import itertools
import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    for P in itertools.product(['', '+', '-'], repeat = N-1):
        num = '1'
        for i, p in enumerate(P):
            num += p + str(i + 2)
        if eval(num) == 0:
            num = '1'
            for i, p in enumerate(P):
                if p == '':
                    num += ' '
                num += p + str(i + 2)
            print(num)
    if t != T-1:
        print()