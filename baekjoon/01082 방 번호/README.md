# [baekjoon_방 번호](https://www.acmicpc.net/problem/1082)


<img width="1158" alt="스크린샷 2022-04-05 오후 3 58 43" src="https://user-images.githubusercontent.com/87896466/161696893-f28c625e-6f72-44a7-9d2d-526a0f914266.png">

## Idea   
>  <a href="/Notes/그리디 알고리즘" target="_blank">Greedy Algorithm (그리디 알고리즘)</a>   
>  숫자가 길수록 즉, 더 많은 숫자를 구매할수록 더 큰 방 번호를 가질 수 있다.   
>  숫자의 길이가 같으면 앞의 숫자가 클수록 더 큰 수가 된다.   

1. 가장 큰 자릿수의 수는 0이 될 수 없으므로 0이 아닌 수들 중 가장 저렴한 숫자를 체크한다.
2. 0을 포함한 숫자들 중 가장 저렴한 숫자를 체크한다.
3. 가장 저렴한 숫자로 길게 숫자를 만든 후 가장 큰자리의 수부터 더 큰 숫자로 바꿀 수 있으면 바꾼다.
