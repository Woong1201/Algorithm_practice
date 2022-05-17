import sys

R, C = map(int, sys.stdin.readline().split())
happy = [list(map(int, sys.stdin.readline().split())) for r in range(R)]

if R % 2 == 1:
    print(('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (R // 2) + 'R' * (C - 1))
elif C % 2 == 1:
    print(('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (C // 2) + 'D' * (R - 1))
else:
    min_val = 1000
    min_loc = [0, 0]
    for r in range(R):
        if r % 2 == 0:
            for c in range(C // 2):
                if happy[r][2*c+1] < min_val:
                    min_val = happy[r][2*c+1]
                    min_loc = [r, 2*c+1]
        else:
            for c in range(C // 2):
                if happy[r][2*c] < min_val:
                    min_val = happy[r][2*c]
                    min_loc = [r, 2*c]
    if min_loc[0] % 2 == 1:
        answer = ('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (min_loc[1] // 2) +\
                'RDLD' * (min_loc[0] // 2) + 'RD' + 'DLDR' * ((R - min_loc[0]) // 2) +\
                ('R' + 'U' * (R - 1) + 'R' + 'D' * (R - 1)) * ((C - 2 - min_loc[1]) // 2)
    else:
        answer = ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (min_loc[0] // 2) +\
                'DRUR' * (min_loc[1] // 2) + 'DR' + 'RURD' * ((C - min_loc[1]) // 2) +\
                ('D' + 'L' * (C - 1) + 'D' + 'R' * (C - 1)) * ((R - 2 - min_loc[0]) // 2)
    print(answer)