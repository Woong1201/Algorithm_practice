# 2630
import sys

def paper(coord, n):
    row = coord[0]
    col = coord[1]
    color = papers[row][col]
    for i in range(n):
        if sum(papers[row+i][col:col+n]) != color*n:
            paper([row, col], n//2)
            paper([row+n//2, col], n//2)
            paper([row, col+n//2], n//2)
            paper([row+n//2, col+n//2], n//2)
            return
    answer[color] += 1

N = int(input())
papers = []
answer = [0, 0]

for i in range(N):
    papers.append(list(map(int, sys.stdin.readline().split())))
paper([0,0], N)

print(answer[0])
print(answer[1])

# 1992
import sys

def Quardtree(coord, n):
    row = coord[0]
    col = coord[1]
    color = video[row][col]
    for i in range(n):
        if video[row+i][col:col+n].count(color) != n:
            return('('+Quardtree([row, col], n//2)+Quardtree([row, col+n//2], n//2)\
                +Quardtree([row+n//2, col], n//2)+Quardtree([row+n//2, col+n//2], n//2)+')')
    else:
        return color

N = int(input())
video = []

for i in range(N):
    video.append(sys.stdin.readline().rstrip())

print(Quardtree([0,0], N))

# 1780
import sys

def paper(coord, n):
    row = coord[0]
    col = coord[1]
    color = papers[row][col]
    for i in range(n):
        if papers[row+i][col:col+n].count(color) != n:
            paper([row, col], n//3)
            paper([row+n//3, col], n//3)
            paper([row+2*n//3, col], n//3)
            paper([row, col+n//3], n//3)
            paper([row+n//3, col+n//3], n//3)
            paper([row+2*n//3, col+n//3], n//3)
            paper([row, col+2*n//3], n//3)
            paper([row+n//3, col+2*n//3], n//3)
            paper([row+2*n//3, col+2*n//3], n//3)
            return
    answer[color] += 1

N = int(input())
papers = []
answer = [0, 0, 0]

for i in range(N):
    papers.append(list(map(int, sys.stdin.readline().split())))
paper([0,0], N)

print(answer[-1])
print(answer[0])
print(answer[1])

# 1629
import sys

def power(n):
    if n == 0:
        return 1
    x = power(n//2)
    if n%2 == 0:
        return x**2%C
    else :
        return x**2*A%C

A, B, C = map(int, sys.stdin.readline().split())
A = A%C

print(power(B)%C)

# 11401


# 2740
import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())
B = []
for i in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(K-1):
        mat = 0
        for k in range(M):
            mat += A[i][k]*B[k][j]
        print(mat, end=' ')
    mat = 0
    for k in range(M):
        mat += A[i][k]*B[k][K-1]
    print(mat)

# 10830


# 11444


# 6549
