# [baekjoon_ACM Craft](https://www.acmicpc.net/problem/1005)   

<img width="1148" alt="스크린샷 2022-05-29 오후 3 49 46" src="https://user-images.githubusercontent.com/87896466/170855963-e97a2551-9b04-48e1-a1f6-8b6548528dd0.png">
<img width="1142" alt="스크린샷 2022-05-29 오후 3 49 55" src="https://user-images.githubusercontent.com/87896466/170855964-f092b683-368d-431f-9125-ac54a4521024.png">

## Idea   
>  <a href="/Notes/다이나믹 프로그래밍" target="_blank">Dynamic Programming (동적계획법)</a>   
>  재귀를 이용하는 top-down 방식의 dp를 적용하여 해결한다.

1. N번 건물을 건설하기 위한 최소 시간을 탐색해보자.   
  N번 건물의 선행 건물들을 모두 조사하여 최소 시간을 찾은 뒤, N번 건물의 건설시간을 더해주면 된다.   
  N번 건물의 선행 건물인 i번 건물의 최소 시간은 i번 건물의 선행 건물들을 모두 조사하면 알 수 있다.
2. 위의 방식을 최종 목표인 W에서 시작하도록 적용하면, W를 건설하기 위한 최소 시간을 알 수 있다.
