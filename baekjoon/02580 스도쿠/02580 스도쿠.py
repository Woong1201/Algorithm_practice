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