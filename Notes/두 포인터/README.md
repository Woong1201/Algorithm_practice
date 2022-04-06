# 두 포인터(Two Pointer)

> 이름 그대로 두 개의 포인터를 사용하여 배열에서 원하는 값을 찾는 방식이다.
> 

## 수들의 합

> N개의 자연수로 이루어진 수열에서 i번째에서 j번째까지의 합이 M이 되는 경우의 수를 구하여라.
> 

```python
import sys

N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
num_M = 0

while start < N:
    sum_array = sum(array[start: end])
    if sum_array == M:
        num_M += 1

    if sum_array > M or end == N:
        start += 1
    elif sum_array <= M:
        end += 1
    
print(num_M)
```

<aside>
🔑 10 5⏎
1 2 3 4 2 5 3 1 1 2⏎
3

</aside>

> 단순 반복문을 사용하게 되면 시간초과가 발생할 수 있다.
위처럼 두 개의 포인터를 사용하게 되면 시간복잡도가 $O(N)$이 되어 해결할 수 있다.
위의 문제는 array의 값들이 모두 자연수이기 때문에 투 포인터로 해결할 수 있다.
> 

## 두 수의 합

> N개의 정수로 이루어진 수열에서 합이 M이 되는 두 개의 수를 찾아라.
> 

```python
import sys

N, M = map(int, input().split())
array = sorted(list(map(int, sys.stdin.readline().split())))
start, end = 0, N - 1

while start < end:
	sum_array = sum(array[start: end])
	if array[start] + array[end] == M:
		break
	if array[start] + array[end] < M:
		start += 1
	if array[start] + array[end] > M:
		end -= 1
if start == end:
	print(-1)
else:
	print(array[start], array[end])
```

<aside>
🔑 10 32⏎
10 20 13 6 19 2 3 14 16 11⏎
13 19

</aside>

> 위처럼 두 포인터가 각각 배열 양 끝에서 시작하는 투 포인터는 정렬된 배열에서 사용가능하다.
>
