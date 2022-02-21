# 2750
import sys
a = int(input())
answer = []
for i in range(a):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in range(a):
    print(answer[i])

# 2751
import sys
a = int(input())
answer = []
for i in range(a):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in range(a):
    print(answer[i])

# 10989
import sys
a = int(input())
b = list(sys.stdin.readlines())
counting_array = [0]*10000
for i in b:
    counting_array[int(i)] += 1
p = 0
while a:
    for i in range(counting_array[p]):
        print(p)
        a-=1

# 2108
import sys
a = int(input())
counting_array = [0]*10000
for i in range(a):
    b = int(sys.stdin.readline())
    counting_array[b] += 1

# 1427
# 11650
# 11651
# 1181
# 10814
# 18870