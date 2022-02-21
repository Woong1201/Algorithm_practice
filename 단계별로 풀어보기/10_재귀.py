# 10872
import math
def factorial(x):
    if x == 0:
        return 1
    else :
        return factorial(x-1)*x
print(factorial(int(input())))

# 10870
def Fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else :
        return Fibonacci(x-1) + Fibonacci(x-2)
print(Fibonacci(int(input())))

# 2447
import math
def star(x, i):
    if x//3 == 1 and i%3 in [2,0]:
        print('***', end='')
    elif x//3 == 1 and i%3 == 1:
        print('* *', end='')
    else :
        if 0 <= i < x//3 or (x//3)*2 <= i < a:
            star(x//3, i%(x//3)), star(x//3, i%(x//3)), star(x//3, i%(x//3))
        else :    
            star(x//3, i%(x//3)), blank(x//3), star(x//3, i%(x//3))
def blank(x):
    if x//3 == 0:
        print(' ', end='')
    else :
        blank(x//3), blank(x//3), blank(x//3)
a = int(input())
b = 0
while(b<a):
    star(a,b)
    print('\n', end='')
    b += 1

# 11729
def Hanoi(p, x, y):
    if p == 1:
        print("{0} {1}".format(x, y))
    else :
        Hanoi(p-1, x, 6//x//y)
        print(x, y)
        Hanoi(p-1, 6//x//y, y)
a = int(input())
print(2**a - 1)
Hanoi(a, 1, 3)