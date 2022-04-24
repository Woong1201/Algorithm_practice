def mat_I(N):
    new_mat = [[0]*N for i in range(N)]
    for i in range(N):
        new_mat[i][i] = 1
    return (new_mat)

def matmul(mat_A, mat_B, N):
    new_mat = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_mat[i][k] = (new_mat[i][k] + mat_A[i][j]*mat_B[j][k])%1000000007
    return (new_mat)

def mat_square(mat, power, N):
    result = mat_I(N)

    while (1 <= power):
        if power % 2 == 1:
            result = matmul(result, mat, 8)
        mat = matmul(mat, mat, 8)
        power = power // 2
    return (result)

D = int(input())

start = [[1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
walks = [[0,1,1,0,0,0,0,0], [1,0,1,1,0,0,0,0], [1,1,0,1,1,0,0,0], [0,1,1,0,1,1,0,0],
         [0,0,1,1,0,1,1,0], [0,0,0,1,1,0,0,1], [0,0,0,0,1,0,0,1], [0,0,0,0,0,1,1,0]]

print (matmul(start, mat_square(walks, D, 8), 8)[0][0])