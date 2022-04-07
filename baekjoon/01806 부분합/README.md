# [baekjoon_부분합](https://www.acmicpc.net/problem/1806)
<img width="1151" alt="스크린샷 2022-04-07 오후 4 42 43" src="https://user-images.githubusercontent.com/87896466/162147282-4f7649b7-e415-4105-aa7a-a7b80680c9dd.png">


## Idea   
>  <a href="/Notes/두 포인터" target="_blank">두 포인터</a>   
>  다른 투 포인터 문제들과 같으나 주어진 시간이 짧으므로 시간을 줄일 방법을 생각해야 한다.

1. array의 부분합을 저장해두고 start, end가 바뀌면 제거되거나 추가되는 array의 원소만 부분합에서 계산해준다.
2. end가 array의 끝에 도달하면 start만 증가시키는데, 부분합이 주어진 값보다 작으면 의미가 없으므로 종료시켜 시간을 단축한다.
