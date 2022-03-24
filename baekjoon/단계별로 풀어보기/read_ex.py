f = open('/Users/gim-yeong-ung/Documents/GitHub/Baekjoon/단계별로 풀어보기/ex.txt', 'r')
lines = f.readlines()
for i in range(len(lines)):
    if i%2==0:
        b = list(lines[i].split())
        print(b[1])