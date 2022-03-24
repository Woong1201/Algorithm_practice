import sys

N, M = map(int, sys.stdin.readline().split())
true = set(list(map(int, sys.stdin.readline().split()))[1:])
false = set(i for i in range(1,N+1)) - true
connect = {i:set() for i in range(1,N+1)}
party = {i:[] for i in range(1,N+1)}

for i in range(M):
    participant = list(map(int, sys.stdin.readline().split()))[1:]
    for j in participant:
        party[j].append(i)
        for p in participant:
            connect[j].add(p)

while len(true):
    true1 = set()
    for i in true:
        for j in connect[i]:
            if j in false:
                false.remove(j)
                true1.add(j)
    true = true1

answer = []
for f in false:
    answer += party[f]

print(len(set(answer)))




import sys

N, M = map(int, sys.stdin.readline().split())

true = set(list(map(int, sys.stdin.readline().split()))[1:])
false = set(i for i in range(1,N+1)) - true

dic = {i:[] for i in range(1,N+1)}
party = []

for i in range(M):
    party.append(set(list(map(int, sys.stdin.readline().split()))[1:]))
    for j in party[-1]:
        dic[j].append(i)

while True:
    over = 0
    if 

    pass

partyset = set()
for t in true:
    partyset.update(dic[t])

print(true, partyset)