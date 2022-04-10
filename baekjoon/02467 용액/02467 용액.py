import sys

N = int(input())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

answer = [0, 0]
if num_list[0] >= 0:
    answer[0], answer[1] = num_list[0], num_list[1]
elif num_list[-1] <= 0:
    answer[0], answer[1] = num_list[-2], num_list[-1]
else:
    start, end = 0, N-1
    sum_num = abs(num_list[start] + num_list[end])
    answer[0], answer[1] = num_list[start], num_list[end]
    while start < end:
        new_sum = num_list[start] + num_list[end]
        if abs(new_sum) < sum_num:
            sum_num = abs(new_sum)
            answer[0], answer[1] = num_list[start], num_list[end]
        if new_sum == 0:
            break
        elif new_sum > 0:
            end -= 1
        else:
            start += 1

print(answer[0], answer[1])