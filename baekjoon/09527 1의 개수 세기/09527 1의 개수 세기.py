import sys
import math

def find_1(x):
    if x in num_dic:
        return
    else:
        y = 2**math.trunc(math.log2(x))
        if y > x:
            y = y//2
        if y not in num_dic:
            find_1(y//2)
            num_dic[y] = num_dic[y//2]*2 + y//2 - 1
        find_1(x-y)
        num_dic[x] = num_dic[y] + (x-y) + num_dic[x-y]

A, B = map(int, sys.stdin.readline().split())
num_dic = {0:0, 1:1, 2:2, 4:5, 8:13, 16:33}

find_1(A-1)
find_1(B)
print(num_dic[B]-num_dic[A-1])