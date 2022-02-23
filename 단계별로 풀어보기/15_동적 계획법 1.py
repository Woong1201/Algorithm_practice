# 1003
import sys
dic = {0 : [1,0], 1:[0,1]}
def fibonacci(x):
    if x not in dic:
        fibonacci(x-1)
        fibonacci(x-2)
        dic[x] = [dic[x-1][0] + dic[x-2][0], dic[x-1][1]+dic[x-2][1]]

a = int(input())
for i in range(a):
    x=(int(sys.stdin.readline()))
    fibonacci(x)
    print(dic[x][0], dic[x][1])

# 9184


# 1904


# 9461


# 1149


# 1932


# 2579


# 1463


# 10844


# 2156


# 11053


# 11054


# 2565


# 9251


# 1912


# 12865