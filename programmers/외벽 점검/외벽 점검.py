import itertools

def solution(n, weak, dist):
    dist.sort(key = lambda x : -x)
    length = [n-weak[-1]+weak[0]]
    for i in range(1, len(weak)):
        length.append(weak[i]-weak[i-1])
    num = 1
    while num <= len(dist):
        pick = itertools.combinations([i for i in range(len(length))], num)
        for p in pick:
            new_length = [sum(length[p[i]+1:p[i+1]]) for i in range(len(p)-1)]
            new_length.append(sum(length[0:p[0]])+sum(length[p[-1]+1:]))
            new_length.sort(key = lambda x : -x)
            clear = 1
            for n in range(len(new_length)):
                if dist[n] < new_length[n]:
                    clear = 0
                    break
            if clear == 1:
                return num
        num += 1
    return -1

n, weak, dist = 12, [1, 5, 6, 10], [1, 2, 3, 4]
n, weak, dist = 200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]
print(solution(n, weak, dist))