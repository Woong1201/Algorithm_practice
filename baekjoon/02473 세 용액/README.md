# [baekjoon_세 용액](https://www.acmicpc.net/problem/2473)   

<img width="1160" alt="스크린샷 2022-04-05 오후 10 30 50" src="https://user-images.githubusercontent.com/87896466/161765159-bc90a1c9-a3a2-4e8f-bdd9-238f96528a11.png">

## Idea   
>  <a href="/Notes/두 포인터" target="_blank">두 포인터</a>, 이분 탐색, 정렬   
>  세 수의 합이 0에 가깝도록 하는 문제이다.   
>  세 번의 반복문이나 combination은 O(N<sup>3</sup>)의 시간복잡도를 가지므로 시간 초과가 될 것 이다.  
>  하나의 수를 선택하고 나머지 두 수를 투 포인터로 선택하여 O(N<sup>2</sup>)의 시간복잡도로 만들었다.   
