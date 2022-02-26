import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    Do = 0
    connect = {} # index : [connected samples]
    weight = {}  # sample : [index, gap]
    while M - Do:
        Do += 1
        case = list(sys.stdin.readline().split())
        case[1] = int(case[1])
        case[2] = int(case[2])
        if case[0] == '!':
            case[3] = -int(case[3])
            if weight.get(case[1], -1) == -1 and weight.get(case[2], -1) == -1:
                connect[case[1]] = [case[1], case[2]]
                weight[case[1]] = [case[1], 0]
                weight[case[2]] = [case[1], -case[3]]
            elif weight.get(case[1], -1) == -1:
                connect[weight[case[2]][0]].append(case[1])
                weight[case[1]] = [weight[case[2]][0], weight[case[2]][1] + case[3]]
            elif weight.get(case[2], -1) == -1:
                connect[weight[case[1]][0]].append(case[2])
                weight[case[2]] = [weight[case[1]][0], weight[case[1]][1] - case[3]]
            else:
                index1 = weight[case[1]][0]
                index2 = weight[case[2]][0]
                if index1 == index2:
                    pass
                elif len(connect[index1]) <= len(connect[index2]):
                    connect[index2] += connect[index1]
                    connect[index1].remove(case[1])
                    for con in connect[index1]:
                        weight[con] = [index2, weight[con][1]-weight[case[1]][1]+case[3]+weight[case[2]][1]]
                    weight[case[1]] = [index2, case[3]+weight[case[2]][1]]
                    del connect[index1]
                else:
                    connect[index1] += connect[index2]
                    connect[index2].remove(case[2])
                    for con in connect[index2]:
                        weight[con] = [index1, weight[con][1]-weight[case[2]][1]-case[3]+weight[case[1]][1]]
                    weight[case[2]] = [index1, -case[3]+weight[case[1]][1]]
                    del connect[index2]
        
        else:
            if weight.get(case[1], -1) == -1 or weight.get(case[2], -1) == -1 or weight[case[1]][0] != weight[case[2]][0]:
                print('UNKNOWN')
            elif weight[case[1]][0] == weight[case[2]][0]:
                print(weight[case[2]][1]-weight[case[1]][1])