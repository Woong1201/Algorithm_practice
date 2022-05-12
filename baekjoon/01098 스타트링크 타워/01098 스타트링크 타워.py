import sys

def impossible_num(str, row):
    impossible = []
    if 1 <= row <= 3 and str[1] == '#':
        impossible.append(0)
    if str[0] == '#' or str[1] == '#':
        impossible.append(1)
    if (row == 1 and (str[0] == '#' or str[1] == '#')) or (row == 3 and (str[1] == '#' or str[2] == '#')):
        impossible.append(2)
    if (row == 1 and (str[0] == '#' or str[1] == '#')) or (row == 3 and (str[0] == '#' or str[1] == '#')):
        impossible.append(3)
    if ((row == 0 or row == 1) and str[1] == '#') or ((row == 3 or row == 4) and (str[0] == '#' or str[1] == '#')):
        impossible.append(4)
    if (row == 1 and (str[1] == '#' or str[2] == '#')) or (row == 3 and (str[0] == '#' or str[1] == '#')):
        impossible.append(5)
    if (row == 1 and (str[1] == '#' or str[2] == '#')) or (row == 3 and str[1] == '#'):
        impossible.append(6)
    if row != 0 and (str[0] == '#' or str[1] == '#'):
        impossible.append(7)
    if (row == 1 or row == 3) and str[1] == '#':
        impossible.append(8)
    if (row == 1 and str[1] == '#') or (row == 3 and (str[0] == '#' or str[1] == '#')):
        impossible.append(9)
    return set(impossible)

N = int(input())
possible_num = [set([0,1,2,3,4,5,6,7,8,9]) for col in range(N)]


for row in range(5):
    floor = sys.stdin.readline().rstrip()
    for col in range(N):
        possible_num[col] -= impossible_num(floor[4*col : 4*col+3], row)

flag = 1
for col in range(N):
    if len(possible_num[col]) == 0:
        print(-1)
        flag = 0
        break

if flag == 1:
    num = 0
    for col in range(N):
        num = num * 10 + (sum(possible_num[col]) / len(possible_num[col]))
    print(num)