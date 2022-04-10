# [baekjoon_용액](https://www.acmicpc.net/problem/2467)   

<img width="1150" alt="스크린샷 2022-04-10 오후 3 16 45" src="https://user-images.githubusercontent.com/87896466/162605118-9725fb1f-8b9d-4b80-82ad-f2e046dd1e3b.png">

## Idea   
>  <a href="/Notes/두 포인터" target="_blank">두 포인터</a>   
>  두 번의 반복문으로 해결하려 하면 시간초과가 생길 것이므로 투 포인터를 사용하는데, 두 포인터가 다른 곳에서 시작하는 문제이다.   
>  주어진 수를 정렬한 뒤 start, end 투 포인터를 활용하여 start위치의 수와 end위치의 수의 합에 따라 포인터를 움직인다.   
>  num[start] + num[end] > 0이면 end -= 1, num[start] + num[end] < 0이면 start += 1을 하여 수의 합이 0에 가까운 수를 찾는다.   
