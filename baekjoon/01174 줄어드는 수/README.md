# [baekjoon_줄어드는 수](https://www.acmicpc.net/problem/1174)   

<img width="1154" alt="스크린샷 2022-05-13 오후 2 06 55" src="https://user-images.githubusercontent.com/87896466/168214920-534abbdd-c55d-438a-b271-7ba1b7433336.png">

## Idea   
>  <a href="/Notes/수학" target="_blank">MATH (수학)</a>   
>  백준에서는 이 문제의 알고리즘을 브루트포스 알고리즘, 백트래킹으로 분류하고 있다.

1. n자리 수 중에서 감소하는 수의 개수는 <sub>10</sub>C<sub>n</sub>개이다.
2. n자리 수 중에서 k번째로 작은 감소하는 수는 '9876543210'에서 n개를 뽑은 수들 중 뒤에서 k번째이다.
3. 위의 두 사실만 알면 위 문제를 쉽게 해결할 수 있다.
