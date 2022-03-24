import itertools
import sys
import copy

def castle(archer, enomy_list):
    kill = 0
    while len(enomy_list):
        death = set()
        for a in archer:
            index = 0
            while index < D:
                for j in range(2*index+1):
                    if j<index and j<len(enomy_list) and 0<=a+j-index<M:
                        if  enomy_list[-1-j][a+j-index] == 1:
                            death.add((-1-j, a+j-index))
                            index = D
                            break
                    elif j>=index and 2*index-j<len(enomy_list) and 0<=a+j-index<M :
                        if enomy_list[-1-2*index+j][a+j-index] == 1:
                            death.add((-1-2*index+j, a+j-index))
                            index = D
                            break
                index += 1

        kill += len(death)
        for i in death:
            enomy_list[i[0]][i[1]] = 0
        del enomy_list[-1]

    return kill

N, M, D = map(int, sys.stdin.readline().split())
enomy = []

for i in range(N):
    enomy.append(list(map(int, sys.stdin.readline().split())))

kills = []
for archer in list(itertools.combinations([i for i in range(M)], 3)): 
    kills.append(castle(archer, copy.deepcopy(enomy)))

print(max(kills))