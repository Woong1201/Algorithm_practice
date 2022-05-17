# [baekjoon_롤러코스터](https://www.acmicpc.net/problem/2873)   

<img width="1159" alt="스크린샷 2022-05-17 오후 3 11 45" src="https://user-images.githubusercontent.com/87896466/168741321-4b2b23c8-474a-4e43-8368-247bad558440.png">
<img width="1155" alt="스크린샷 2022-05-17 오후 3 11 53" src="https://user-images.githubusercontent.com/87896466/168741332-8f892c0b-94a0-4b8f-a1c6-d98acbd704e3.png">

## Idea   
>  <a href="/Notes/구현" target="_blank">Implementation (구현)</a>   
>  행, 열의 개수 중 하나라도 홀수라면 모든 칸을 지나칠 수 있고 행, 열의 개수가 모두 짝수인 경우에는 딱 한 칸을 지나가지 못한다.

1. 행, 열의 개수를 판단한다.
2. 행, 열의 개수가 모두 짝수인 경우 지나치지 않을 한 칸을 고르는데, 그 칸의 (행+열)은 홀수여야 한다.
3. 경로를 출력한다.
