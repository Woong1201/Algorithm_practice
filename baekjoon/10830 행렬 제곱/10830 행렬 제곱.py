import sys

N, B = map(int, sys.stdin.readline().split())
mat = []

for i in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))

def mat_I(N):
    new_mat = [[0]*N for i in range(N)]
    for i in range(N):
        new_mat[i][i] = 1
    return (new_mat)

def matmul(mat_A, mat_B):
    new_mat = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_mat[i][k] = (new_mat[i][k] + mat_A[i][j]*mat_B[j][k])%1000
    return (new_mat)

answer = mat_I(N)

while (1 <= B):
    if B % 2 == 1:
        answer = matmul(answer, mat)
    mat = matmul(mat, mat)
    B = B // 2

for i in range(N):
    for j in range(N - 1):
        print(answer[i][j], end = ' ')
    print(answer[i][N-1])