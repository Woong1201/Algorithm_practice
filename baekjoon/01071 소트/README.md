# [baekjoon_소트](https://www.acmicpc.net/problem/1071)   

<img width="1147" alt="스크린샷 2022-04-09 오전 2 43 10" src="https://user-images.githubusercontent.com/87896466/162494236-bf5add45-7a5d-4409-b8d4-949143e12189.png">


## Idea   
>  <a href="/Notes/그리디 알고리즘" target="_blank">Greedy Algorithm (그리디 알고리즘)</a>   
>  수열을 정렬하고 *탐욕적으로*  앞의 숫자부터 조건에 어긋나는 부분만 바꿔주면 해결할 수 있다.

1. 주어진 수열을 정렬한다.   
2. 정렬된 수열의 수들을 순서대로 다음의 규칙에 맞게 새로운 수열에 넣는다.
  - 새로운 수열에 blank가 있고 blank에 수를 넣을 수 있으면 (입력하려는 수가 blank 이전의 숫자+1이 아니라면) blank 위치에 새로운 수를 넣는다. 
  - 새로운 수열에 넣으려는 수가 (새로운 수열의 마지막 숫자+1)이라면 blank와 수를 새로운 수열 맨 뒤에 함께 넣는다. (blank가 이미 있으면 발생 불가.)
  - 위에 해당하지 않으면 새로운 수열 뒤에 수를 넣는다.
3. 위의 작업이 끝난 뒤, blank가 있다면 blank앞의 수와 뒤의 수의 자리를 바꾼다.(같은 수가 연속하여 있다면 연속한 같은 수들도 함께)
<!-- 
1. 주어진 수열을 정렬한다.   
2. 정렬된 수열의 수들을 순서대로 다음의 규칙에 따라 새로운 수열에 입력한다.
  - 입력하려는 수를 num, blank의 정보를 blank_idx (blank의 위치, 존재하지 않으면 -1), 새로운 수열을 new_list라 하자.
  - blank != -1, new_list[blank-1] + 1 != num => new_list[blank] = num 
  - new_list[-1] + 1 != num => blank_idx = len(new_list), new_list += [-1, num]
  - 위에 해당하지 않으면 new_list.append(num)
3. 마지막 숫자까지 새로운 수열에 넣었는데, blank가 남았다면 blank앞의 수와 뒤의 수의 자리를 바꾼다.(같은 수가 연속하여 있다면 연속한 같은 수들을 함께) -->
