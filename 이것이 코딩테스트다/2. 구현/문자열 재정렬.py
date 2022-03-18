import re
import sys

string = sorted(re.split('', sys.stdin.readline().rstrip())[1:-1])
num = 0

for index, s in enumerate(string):
    if s.isalpha():
        break
    num += int(s)

print(''.join(string[index:]) + str(num))