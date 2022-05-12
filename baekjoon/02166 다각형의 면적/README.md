# [baekjoon_다각형의 면적](https://www.acmicpc.net/problem/2166)   
<img width="1168" alt="스크린샷 2022-05-12 오후 8 35 13" src="https://user-images.githubusercontent.com/87896466/168066413-f785d1d7-a2e4-449d-bf70-16eec8c4f7b8.png">


## Idea   
>  <a href="/Notes/수학" target="_blank">MATH (수학)</a>   
>  두 벡터의 외적으로 삼각형의 넓이를 구할 수 있다.

1. 원점과 주어진 점들의 벡터를 각각 구하고, 주어진 순서에서 연속하는 두 벡터를 가지고 외적을 구한다.
(마지막 점은 첫번째 점과의 외적을 구한다.)
2. (모든 외적의 합 * 1/2)이 구하려는 다각형의 넓이와 같다.
