# 15649
import itertools
N, M = map(int, input().split())
x = list(itertools.permutations([str(i) for i in range(1, N+1)], M))
for i in x:
    print(' '.join(i))

# 15650
import itertools
N, M = map(int, input().split())
x = list(itertools.combinations([str(i) for i in range(1, N+1)], M))
for i in x:
    print(' '.join(i))

# 15651
import itertools
N, M = map(int, input().split())
x = list(itertools.product([str(i) for i in range(1, N+1)], repeat = M))
for i in x:
    print(' '.join(i))

# 15652
import itertools
N, M = map(int, input().split())
x = list(itertools.combinations_with_replacement([str(i) for i in range(1, N+1)], M))
for i in x:
    print(' '.join(i))

# 9663
N = int(input())
if N==1:
    print(1)
    step = -1
else :
    step = 1
N_Queen = [0]
answer = 0
while True:
    if step == -1:
        print(answer)
        break
    else:
        p = -1
        if len(N_Queen)==step:
            N_Queen.append(-1)
        for j in range(N_Queen[step]+1, N):
            for i in range(step):
                if j == N_Queen[i]:
                    break
                elif j+step == i+N_Queen[i] or j-step == N_Queen[i]-i:
                    break
            else:
                N_Queen[step] = j
                p=0
                if step == N-1:
                    answer+=1
                    N_Queen.pop()
                    step-=1
                    if N_Queen[-1] == N-1:
                        N_Queen.pop()
                        step -= 1
                else:
                    step += 1
                break
        if p==-1:
            N_Queen.pop()
            step -= 1
            if N_Queen[-1] == N-1:
                N_Queen.pop()
                step -= 1






# 2580

# 14888

# 14889