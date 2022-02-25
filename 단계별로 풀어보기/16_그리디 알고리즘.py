# 11047
import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = []
num = 0

for i in range(N):
    coin_list.append(int(sys.stdin.readline()))

while K:
    coin = coin_list.pop()
    num += K//coin
    K = K%coin

print(num)

# 1931
import sys

N = int(input())
meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)])

index = 0
while index<len(meeting)-1:
    if meeting[index+1][1] < meeting[index][1]:
        del(meeting[index])
        if index!=0:
            index -= 1
    elif meeting[index][1] == meeting[index+1][1] and meeting[index+1][0]!=meeting[index+1][1]:
        del(meeting[index])
        if index!=0:
            index -= 1
    elif meeting[index+1][0] == meeting[index][0] and meeting[index][0]!=meeting[index][1]:
        del(meeting[index+1])
    else:
        index+=1

max = 0
time = 0
for meet in meeting:
    if meet[0] >= time:
        max += 1
        time = meet[1]
print(max)

# 11399
import sys
N = int(input())
people = sorted(list(map(int, sys.stdin.readline().split())))
time = 0

for i in range(N):
    time += people[i]*(N-i)

print(time)

# 1541
import sys
formular = sys.stdin.readline().rstrip()
num1 = []
num2 = []
minus = formular.find('-')
if minus == -1:
    minus = len(formular) + 1
start = 0
for i in range(len(formular)+1):
    if i == len(formular) or not formular[i].isdigit():
        if i <= minus:
            num1.append(int(formular[start:i]))
            start = i+1
        else:
            num2.append(int(formular[start:i]))
            start = i+1

print(sum(num1)-sum(num2))

# 13305
import sys

N = int(input())
road = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
min = oil[0]

for i in range (len(oil)):
    if oil[i] < min:
        min = oil[i]
    else:
        oil[i] = min

print(sum(oil[i]*road[i] for i in range(N-1)))