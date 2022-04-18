# [baekjoon_극적인 곱셈](https://www.acmicpc.net/problem/1979)   

<img width="1148" alt="스크린샷 2022-04-14 오후 7 59 01" src="https://user-images.githubusercontent.com/87896466/163757707-064345b5-7ad7-4f15-aed6-0d9a8f89b841.png">

## Idea   
>  <a href="/Notes/수학" target="_blank">MATH (수학)</a>, 임의 정밀도 / 큰 수 연산   
>  극적인 숫자가 없는 경우를 열심히 생각했는데, 단순하게 n > k 였다.   
>  극적인 숫자를 구하는 것은 간단하다. n을 곱하고 10으로 나누어 몫과 나머지를 구하는 과정을 여러번 하며 구하면 된다.   
>  a<sub>n</sub> = (a<sub>n-1</sub>%10)\*n + a<sub>n-1</sub>//10, a<sub>0</sub> = k에 대하여   
>  a<sub>n</sub> = k, n != 0 를 만족하는 최솟값n을 구하면 극적인 수는 a<sub>n-1</sub>a<sub>n-1</sub> ... a<sub>1</sub>a<sub>0</sub>이다.

아래 코드는 극적인 숫자가 없는 경우를 고민한 코드이다.   
1부터 99까지의 숫자를 체크하며 k값이 계산 중에 나오는지 확인하는데 모든 숫자를 확인해도 k값이 안나오는 경우에 극적인 숫자가 없는 것이다.   
위에서 내린 결론처럼 저 긴 코드를 if (n > k)로 처리하여 해결했다.   
(코드를 다 쓰기 전에 저 긴 코드가 n > k를 의미함을 깨달았다면 뿌듯했을텐데..)   

```python
from collections import deque

n, k = map(int, input().split())
max_range = 9 * (n + 1)
visited_num = [0]*100
visited_num[10*k] = 1
nums = deque([k])
pos = 0

while nums and pos==0:
    num = nums.popleft()
    for i in range(9):
        new_num = 10*i + (num-i)//n 
        if (num-i)//n >= 10 or (num - i) % n != 0 or visited_num[new_num]==1:
            continue
        if new_num == k:
            pos = 1
            break
        elif new_num <= max_range:
            nums.append(new_num)                
        visited_num[new_num] = 1
if pos == 0:
    print(0)
```
