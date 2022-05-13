import itertools
import math

N = int(input())
len = 1
while True:
    if len > 10:
        print(-1)
        break
    elif N > math.comb(10, len):
        N -= math.comb(10, len)
        len += 1
    else:
        print(''.join(list(itertools.combinations('9876543210', len))[-N]))
        break