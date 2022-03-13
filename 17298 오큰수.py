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