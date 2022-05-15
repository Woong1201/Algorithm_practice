# [baekjoon_0 만들기](https://www.acmicpc.net/problem/7490)   

<img width="1157" alt="스크린샷 2022-05-15 오후 5 49 00" src="https://user-images.githubusercontent.com/87896466/168464851-51667bdb-7af5-4cff-be3d-06e964a20df9.png">
<img width="1153" alt="스크린샷 2022-05-15 오후 5 49 06" src="https://user-images.githubusercontent.com/87896466/168464861-dd68becc-c3e6-4cb0-bc8f-6f9fb5bdaee4.png">


## Idea   
>  <a href="/Notes/구현" target="_blank">Implementation (구현)</a>   
>  파이썬의 내장 라이브러리 함수인 eval()과 itertools 라이브러리의 product 함수를 활용한다.

1. 주어지는 수 N에 대하여 \['', '+', '-'] 중 중복을 포함하여 N-1개를 선택하여 N개의 수들 사이에 넣어주고 eval함수로 계산한다.
2. 이때 계산한 값이 0이면 그 문자열을 출력하면 된다.
