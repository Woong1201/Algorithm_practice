import sys

number = sys.stdin.readline().rstrip()
length = len(number)

num = 0
for n in number[:length//2]:
    num += int(n)
for n in number[length//2:]:
    num -= int(n)

if num == 0:
    print('LUCKY')
else:
    print('READY')