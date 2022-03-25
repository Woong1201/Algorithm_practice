#  <a href="https://programmers.co.kr/learn/courses/30/lessons/60062" target="_blank">programmers_외벽 점검</a>

<img width="1436" alt="스크린샷 2022-03-25 오후 3 48 03" src="https://user-images.githubusercontent.com/87896466/160073356-a2458009-9647-4010-9a61-4efd4381656d.png">

> ## Idea  
> 두 weak 사이의 거리가 dist원소의 값보다 작으면 그 weak들을 포함하여 사이에 있는 weak들을 한 명의 친구가 점검할 수 있다.   
> weak 사이의 외벽을 모두 점검할 필요는 없다. => weak 사이의 거리를 리스트로 만들고 그 중 몇 개를 제거하여 해결한다.
1. dist를 내림차순으로 정렬한다.
2. weak에서 연속하는 두 점 사이의 거리들을 length에 순서대로 저장한다.
- length[i] = distance(weak의 i번째 원소, weak의 (i-1)번째 원소)
3. length의 원소를 n개로 분할하여 각 분할의 합을 new_length에 내림차순으로 저장한다.
- length의 원소 n개를 택하여 제거하면 제거된 원소 사이의 값들이 각 분할이 되고, 그 합을 계산한다.
- 외벽은 원형이므로 length의 양끝 값은 연결되어 있고, 제거된 원소 중 양 끝에 있는 원소 사이에 들어가게 된다.
- ex) length=[1,2,3,4,5,6,7] 에서 2, 6 원소가 제거되면 [7,1],[3,4,5]로 분할되고 new_length=[12, 8]이 된다. 
4. dist 중 n개의 원소 와 new_length의 원소들을 순서대로 비교했을때, 모두 (dist의 원소) > (new_length의 원소) 이면 외벽점검을 성공한다.

<!-- ex)
n, weak, dist = 12, [1, 5, 6, 10], [1, 2, 3, 4]
1. dist = [4, 3, 2, 1]
2. length = [3, 4, 1, 4] # length[0] : 10 과 1 사이의 거리
3. +num = 1, new_length = [9], [8], [11], [8] # length의 원소를 하나씩 제거한 경우이다.   
  +num = 2, new_length = [0, 5], [4, 4], [5, 0], [0, 7], [3, 1], ... # length의 원소를 두개 씩 제거한 경우이다.
4. num = 2, new_length = [3, 1] 일때, dist = [4, 3] 과 비교하여 dist의 원소들이 크기 때문에 num = 2 가 return된다. -->
