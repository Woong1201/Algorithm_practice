# 15596
def solve(a):
    return sum(a)

# 4673
not_self_set =set()
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                not_self_set.add(1001*i + 101*j + 11*k + 2*l)
for i in range(1, 10001):
    if not(i in not_self_set):
        print(i)

# 1065
a = int(input())
if a < 100:
    print(a)
else:
    p = 99
    for i in range(101, a+1):
        if ((i%100)//10)*2 == (i//100) + (i%10):
            p += 1
    print(p)