import itertools
import math

N = int(input())
if N >= 2**10-1:
    print(-1)
else:
    for i in range(1, 11):
        if N >= math.comb(10, i):
            N -= math.comb(10, i)
        else:
            print(''.join(sorted(list(itertools.combinations([str(i) for i in range(9, -1, -1)], i))[-1-N], key = lambda x : -int(x))))
            break