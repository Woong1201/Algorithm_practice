# [baekjoon_감소하는 수](https://www.acmicpc.net/problem/1038)   

<img width="1151" alt="스크린샷 2022-05-13 오후 2 16 05" src="https://user-images.githubusercontent.com/87896466/168215852-4d6e674a-c5bb-419b-9c9e-4a5b59c72536.png">

## Idea   
>  <a href="/Notes/수학" target="_blank">MATH (수학)</a>   
>  백준에서는 이 문제의 알고리즘을 브루트포스 알고리즘, 백트래킹으로 분류하고 있다.

1. n자리 수 중에서 감소하는 수의 개수는 <sub>10</sub>C<sub>n</sub>개이다.
2. n자리 수 중에서 k번째로 작은 감소하는 수는 '9876543210'에서 n개를 뽑은 수들 중 뒤에서 k번째이다.
3. 위의 두 사실만 알면 위 문제를 쉽게 해결할 수 있다.
