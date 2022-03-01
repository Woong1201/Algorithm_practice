# 10828
import sys

N = int(input())
stack = []
for i in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else :
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 10773
import sys

K = int(input())
stack = []

for i in range(K):
    number = int(sys.stdin.readline())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))

# 9012
import sys

K = int(input())

for i in range(K):
    string = sys.stdin.readline().rstrip()
    VPS = 0
    for s in string:
        if s == '(':
            VPS += 1
        else:
            VPS -= 1
        if VPS < 0:
            break
    if VPS == 0:
        print('YES')
    else:
        print('NO')

# 4949
import sys

bracket_list = ['(', ')', '[', ']']    
while True:
    string = sys.stdin.readline()
    bracket = []
    if string == '.\n':
        break
    
    for s in string:
        if s in bracket_list:
            if s in ['(', '[']:
                bracket.append(s)
            elif len(bracket) == 0 or (bracket[-1] =='(' and s == ']') or (bracket[-1] == '[' and s == ')'):
                bracket = ['NO']
                break
            else:
                del bracket[-1]

    if len(bracket) == 0:
        print('yes')
    else:
        print('no')

# 1874
import sys

n = int(input())
num_list = []
stack = []
index = 1
impossible = 0

for i in range(n):
    num = int(sys.stdin.readline())
    if num >= index:
        stack += (['+']*(num-index+1)+['-'])
        num_list += [j for j in range(index, num)]
        index = num + 1
    elif num_list[-1] == num:
        stack.append('-')
        del num_list[-1]
    else:
        impossible = 1
        break

if impossible == 1:
    print('NO')
else:
    for cal in stack:
        print(cal)

# 17298
import sys

N = int(input())
number = list(map(int, sys.stdin.readline().split()))
stack = []

for i in range(N-1):
    if number[i] < number[i+1]:
        number[i] = number[i+1]
        while len(stack):
            if stack[-1][1] < number[i+1]:
                number[stack.pop()[0]] = number[i+1]
            else:
                break

    else:
        stack.append([i, number[i]])
        number[i]=-1
        
for i in number[:-1]:
    print(i, end=' ')
print(-1)