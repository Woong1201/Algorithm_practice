#  <a href="https://programmers.co.kr/learn/courses/30/lessons/60060" target="_blank">programmers_가사 검색</a>

<img width="1417" alt="스크린샷 2022-04-07 15 39 37" src="https://user-images.githubusercontent.com/87896466/162136756-08c1a425-245c-4f2a-898c-986cfe0b4863.png">

> ## Idea  
>  <a href="/Notes/이진 탐색" target="_blank">이진 탐색</a>  
> word 길이에 따라 사전을 달리하여 만들고 탐색한다.   
> '?'가 query뒤에 있는 경우 뒤집어서 탐색할 것이고, 따라서 사전을 만들때에도 단어를 뒤집은 사전을 만든다.

1. word들을 입력받아 단어길이에 따라 사전에 넣은 후, 각 사전을 정렬한다.
2. query들을 순서대로 확인하며 해당하는 단어의 수를 탐색한다.
- 이때, bisect함수로 이진탐색을 하여 시간을 단축한다.
