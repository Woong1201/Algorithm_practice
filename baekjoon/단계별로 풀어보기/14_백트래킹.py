# 15649
import itertools
N, M = map(int, input().split())
x = list(itertools.permutations([str(i) for i in range(1, N+1)], M))
for i in x:
    print(' '.join(i))

# 15650
import itertools
N, M = map(int, input().split())
x = list(itertools.combinations([str(i) for i in range(1, N+1)], M))
for i in x:
    print(' '.join(i))

# 15651
import itertools
N, M = map(int, input().split())
x = list(itertools.product([str(i) for i in range(1, N+1)], repeat = M))
for i in x:
    print(' '.join(i))

# 15652
import itertools
N, M = map(int, input().split())
x = list(itertools.combinations_with_replacement([str(i) for i in range(1, N+1)], M))
for i in x:
    print(' '.join(i))

# 9663
N = int(input())
answer = 0
N_Queen = [0] * N

def is_Queen(step):
    p, q = step, N_Queen[step]
    for i, j in enumerate(N_Queen[:step]):
        if j==N_Queen[step] or i+j == step+N_Queen[step] or i-j == step-N_Queen[step]:
            return False
    return True

def Queen(x):
    global answer
    if x == N:
        answer += 1
    else :
        for i in range(N):
            N_Queen[x] = i
            if is_Queen(x):
                Queen(x+1)

Queen(0)
print(answer)

# 2580
import sys

def check_sdoku(x, val):
    i, j = x[0], x[1]
    for p in range (9):
        if p!=j and sdoku[i][p] == val:
            return False
        if p!=i and sdoku[p][j] == val:
            return False
        if i!= 3*(i//3)+p//3 and j!= 3*(j//3)+p%3 and sdoku[3*(i//3)+p//3][3*(j//3)+p%3] == val:
            return False
    return True

def final_sdoku(n):
    global out
    if out == 1:
        return
    if n == l:
        out = 1
        for i in range(9):
            ans = ''
            for j in range(9):
                ans += (str(sdoku[i][j])+' ')
            print(ans[:-1])
    else :
        for i in dic[dic_key[n]]:
            sdoku[dic_key[n][0]][dic_key[n][1]] = i
            if check_sdoku(dic_key[n], i):    
                final_sdoku(n+1)
        sdoku[dic_key[n][0]][dic_key[n][1]] = 0

sdoku = []
dic = {}
for i in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().split())))
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            dic_sdoku = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for p in range (9):
                if sdoku[i][p] in dic_sdoku:
                    dic_sdoku.remove(sdoku[i][p])
                if sdoku[p][j] in dic_sdoku:
                    dic_sdoku.remove(sdoku[p][j])
                if sdoku[3*(i//3)+p//3][3*(j//3)+p%3] in dic_sdoku:
                    dic_sdoku.remove(sdoku[3*(i//3)+p//3][3*(j//3)+p%3])
            dic[(i,j)] = dic_sdoku

while dic:
    for x in dic:
        if len(dic[x]) == 1:
            i, j, val = x[0], x[1], dic[x][0]
            sdoku[i][j] = val
            del(dic[x])
            for p in range(9):
                if (i,p) in dic and val in dic[(i,p)]:
                    dic[(i,p)].remove(val)
                if (p,j) in dic and val in dic[(p,j)]:
                    dic[(p,j)].remove(val)
                if (3*(i//3)+p//3, 3*(j//3)+p%3) in dic and val in dic[(3*(i//3)+p//3, 3*(j//3)+p%3)]:
                    dic[(3*(i//3)+p//3, 3*(j//3)+p%3)].remove(val)
            break
    else:
        break

dic_key = list(dic.keys())
l = len(dic_key)
out = 0
final_sdoku(0)

# 14888
import itertools
import sys

a = int(input())
num = list(map(int,sys.stdin.readline().split()))
cal_num = list(map(int,sys.stdin.readline().split()))
set_a = set(i for i in range(1, a))
max = -1000000000
min = 1000000000

per1 = set(itertools.combinations(set_a, cal_num[0]))
for i in per1:
    i = set(i)
    per2 = set(itertools.combinations(set_a - i, cal_num[1]))
    for j in per2:
        j = set(j)
        per3 = set(itertools.combinations(set_a - i - j, cal_num[2]))
        for k in per3:
            k = set(k)
            ans = num[0]
            for p in range(1, a):
                if p in i:
                    ans += num[p]
                elif p in j:
                    ans -= num[p]
                elif p in k:
                    ans *= num[p]
                else:
                    if ans >= 0:
                        ans = ans // num[p]
                    else:
                        ans = -((-ans) // num[p])
            if ans > max:
                max = ans
            if ans < min:
                min = ans
print(max)
print(min)

# 14889
import itertools
import sys
N = int(input())
stat = {}

for i in range(N):
    b = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        stat[(i,j)] = b[j]

min = 40000
member = set(i for i in range(1, N))
per = set(itertools.combinations(member, N//2-1))

for i in per:
    team1 = set(i) | set([0])
    team2 = member - team1
    s = 0
    for i in team1:
        for j in team1:
            s += stat[(i,j)]
    for i in team2:
        for j in team2:
            s -= stat[(i,j)]
    if abs(s) < min:
        min = abs(s)
print(min)