import sys

N = int(input())
num = sys.stdin.readline().split()
dic = {}
num_set = set(num)

for i in range (1, N):
    a = int(num[i])
    for j in range (0, i):
        b = int(num[j])
        if (b, a-b) in dic:
            dic[(a,a-b)] = dic.pop((b,a-b)) + a
        elif str(2*a-b) in num_set:
            dic[(a,a-b)] = a + b

print(max(list(dic.values())+[0]))