# 1330
a, b = map(int, input().split())
if a > b:
    print(">")
elif a == b:
    print("==")
else :
    print("<")

# 9498
a = int(input())
if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("F")

# 2753
a = int(input())
if a % 4 == 0:
    if a % 100 != 0 or a % 400 == 0:
        print(1)
    else :
        print(0)
else :
    print(0)

# 14681
a = int(input())
b = int(input())
if a > 0:
    if b > 0:
        print(1)
    else :
        print(4)
else :
    if b > 0:
        print(2)
    else :
        print(3)

# 2884
a, b = map(int, input().split())
if b < 45 :
    if a == 0:
        print(23, b+15)
    else:
        print(a-1, b+15)
else :
    print(a, b-45)

# 2525
a, b = map(int, input().split())
c = int(input())
a += c//60
b += c%60
if b >= 60:
    b -= 60
    a += 1
print(a%24, b)

# 2480
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + 1000*a)
elif a == b or a == c:
    print(1000 + 100*a)
elif b == c:
    print(1000 + 100*b)
else :
    print(100*max(a,b,c))