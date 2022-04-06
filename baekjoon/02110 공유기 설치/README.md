# [baekjoon_공유기 설치](https://www.acmicpc.net/problem/2110)   
## Idea   

<img width="1168" alt="스크린샷 2022-04-06 오후 7 53 12" src="https://user-images.githubusercontent.com/87896466/161959402-1b764f9f-a6ac-497e-baf4-da0eb505a5c7.png">

>  <a href="/Notes/이진 탐색" target="_blank">이진 탐색</a>, 매개 변수 탐색   
>  '최소 거리'를 설정하고 그에 맞게 집을 선택할 수 있는지 확인한다.

1. 집을 선택하는 방법을 고민했는데 딱히 할 수 있는게 없는 것 같아 '최소 거리'를 설정하니 풀 수 있었다.
2. 선택한 '최소 거리'에 맞게 집을 선택, 공유기를 설치할 수 있으면 '최소 거리'를 늘리고 아니면 줄이는데 이때 이분 탐색을 사용한다.
