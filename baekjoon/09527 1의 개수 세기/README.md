# [baekjoon_1의 개수 세기](https://www.acmicpc.net/problem/9527)   

<img width="1155" alt="스크린샷 2022-04-08 오후 5 38 25" src="https://user-images.githubusercontent.com/87896466/162398736-45921553-3e67-4b04-b678-74c4dcf685b5.png">

## Idea   
>  <a href="/Notes/수학" target="_blank">MATH (수학)</a>, 누적 합   
>  이진수는 2의 거듭제곱마다 반복되는 패턴이 있다.   
>  &nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;&nbsp;&nbsp;&nbsp;1,&nbsp;&nbsp;&nbsp;10,&nbsp;&nbsp;&nbsp;11    　　0부터 3까지를 이진수로 나타낸 수들 앞에 각각 1을 붙이면   
>  100, 101, 110, 111    　　4에서 7까지를 이진수로 나타낸 것과 같다.

1. find_1(x)를 0부터 x까지의 수를 이진수로 나타냈을 때 1의 개수라 하자.
- 이때 초기값과 계산과정 중에 구한 값들을 dic에 저장하여 시간을 단축한다. {0:0, 1:1, 2:2, 4:5}
2. find_1(x) = find_1(2<sup>int(log<sub>2</sub>x)</sup>) + (x-2<sup>int(log<sub>2</sub>x)</sup>) + find_1(x-2<sup>int(log<sub>2</sub>x)</sup>)
- (x보다 크지 않은 2의 거듭제곱 중 가장 큰 수 = 2<sup>int(log<sub>2</sub>x)</sup>)에서 x까지 이진수로 나타냈을때 몇개의 1이 추가되는지 생각하면 위의 식을 찾을 수 있다.
- 이때 문제에서 입력하는 숫자의 범위가 크기 때문에, int(log<sub>2</sub>x)에서 버림이 아닌 올림을 하는 경우가 생기므로       
이를 방지하는 함수를 추가하거나 log가 아닌 다른 방법으로 2<sup>int(log<sub>2</sub>x)</sup>를 찾아야 한다.
3. 주어진 두 수 A, B에 대하여 find_1(B) - find_1(A-1)을 계산하면 마무리된다.
