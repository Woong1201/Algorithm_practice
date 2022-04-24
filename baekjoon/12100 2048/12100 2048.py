import itertools
import sys

def rotate(m):
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret

def game(move, board):
    new_board = board.copy()
    
    for i in move:
        if i == 'L':
            for row in range(N):
                line = []
                for col in range(N):
                    if new_board[row][col]!=0:
                        line.append(new_board[row][col])
                col = 0
                new_line = []
                while col < len(line)-1:
                    if line[col] == line[col+1]:
                        new_line.append(line[col]*2)
                        col += 2
                    else:
                        new_line.append(line[col])
                        col += 1
                if col == len(line)-1:
                    new_line.append(line[col])
                new_line += [0]*(N-len(new_line))
                new_board[row] = new_line

        if i == 'R':
            for row in range(N):
                line = []
                for col in range(N-1, -1, -1):
                    if new_board[row][col] != 0:
                        line.append(new_board[row][col])
                col = 0
                new_line = []
                while col < len(line)-1:
                    if line[col] == line[col+1]:
                        new_line.append(line[col]*2)
                        col += 2
                    else:
                        new_line.append(line[col])
                        col += 1
                if col == len(line)-1:
                    new_line.append(line[col])
                new_line += [0]*(N-len(new_line))
                new_board[row] = list(reversed(new_line))

        elif i == 'U':
            x = []
            for col in range(N):
                line = []
                for row in range(N):
                    if new_board[row][col]!=0:
                        line.append(new_board[row][col])
                row = 0
                new_line = []
                while row < len(line)-1:
                    if line[row] == line[row+1]:
                        new_line.append(line[row]*2)
                        row += 2
                    else:
                        new_line.append(line[row])
                        row += 1
                if row == len(line)-1:
                    new_line.append(line[row])
                new_line += [0]*(N-len(new_line))
                x.append(list(reversed(new_line)))
            new_board = rotate(x)
        
        if i == 'D':
            x = []
            for col in range(N):
                line = []
                for row in range(N-1, -1, -1):
                    if new_board[row][col] != 0:
                        line.append(new_board[row][col])
                row = 0
                new_line = []
                while row < len(line)-1:
                    if line[row] == line[row+1]:
                        new_line.append(line[row]*2)
                        row += 2
                    else:
                        new_line.append(line[row])
                        row += 1
                if row == len(line)-1:
                    new_line.append(line[row])
                new_line += [0]*(N-len(new_line))
                x.append(new_line)
            new_board = rotate(x)
            
    return max(max(line) for line in new_board)

N = int(input())
board = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

max_val = 0
moves = list(itertools.product(['L','R','U','D'], repeat=5))

for move in moves:
    max_val = max(max_val, game(move, board))

print(max_val)

# 4
# 2 2 4 16
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0