# 11654
print(ord(input()))

# 11720
a = int(input())
b = int(input())
answer = 0
for i in range(a):
    answer += b%10
    b = b//10
print(answer)

# 10809
a = input()
answer = ''
for i in range(97, 123):
    answer += str(a.find(chr(i)))
    answer += ' '
print(answer[:-1])

# 2675
import sys
a = int(input())
for i in range(a):
    b, c = sys.stdin.readline().split()
    d = ""
    for j in c:
        d += j*int(b)
    print(d)

# 1157
a = input().upper()
answer = ['?', 0]
for i in range (65, 91):
    if a.count(chr(i)) == answer[1]:
        answer[0] = '?'
    elif a.count(chr(i)) > answer[1]:
        answer[0] = chr(i)
        answer[1] = a.count(chr(i))
print(answer[0])

# 1152
import sys
a = list(sys.stdin.readline().split())
print(len(a))

# 2908
import sys
a, b = sys.stdin.readline().split()
print(max(a[::-1], b[::-1]))

# 5622
import sys
a = sys.stdin.readline()
dic = {'A':3, 'B':3, 'C':3, 'D':4, 'E':4, 'F':4, 'G':5, 'H':5, 'I':5, 'J':6, 'K':6, 'L':6, 'M':7, 'N':7, 'O':7,
        'P':8, 'Q':8, 'R':8, 'S':8, 'T':9, 'U':9, 'V':9, 'W':10, 'X':10, 'Y':10, 'Z':10, '\n':0}
answer = 0
for i in a:
    answer += dic[i]
print(answer)

# 2941
import sys
a = sys.stdin.readline()[:-1]
set_c= ['c=', 'c-','d-', 'lj', 'nj', 's=', 'dz=', 'z=']
p = 0
for i in set_c:
    p += a.count(i)
print(len(a)-p)

# 1316
import sys
a = int(input())
answer = 0
for i in range(a):
    b = sys.stdin.readline()
    p = 0
    while b[p]!='\n':
        if b[p] != b[p+1] and (b[p] in b[p+1:]):
            answer += 1
            break
        p+=1
print(a - answer)