# [baekjoon_blobaww](https://www.acmicpc.net/problem/24501)

<img width="1155" alt="스크린샷 2022-05-10 오후 4 04 34" src="https://user-images.githubusercontent.com/87896466/167568561-b171adaa-3254-4f94-8d8f-a43873512681.png">
<img width="1156" alt="스크린샷 2022-05-10 오후 4 04 41" src="https://user-images.githubusercontent.com/87896466/167568565-d190b1b0-6305-429e-b1bf-2f7ab68faba8.png">

## Idea
> <a href="/Notes/다이나믹 프로그래밍" target="_blank">Dynamic Programming(동적 계획법) </a>   
> 주어진 행렬에서 경우의 수를 순차적으로 탐색하는데, 이전까지의 저장된 값을 바탕으로 현재 칸에서의 경우의 수를 구한다.

1. (x,y) 까지의 E를 누르는 경우의 수를 E(x,y)라 하면 E(x,y) = E(x-1, y) + E(x, y-1) - E(x-1, y-1) + (ESM(x,y) == E)
2. (x,y) 까지의 E, S를 누르는 경우의 수를 S(x,y)라 하면 S(x,y) = S(x-1, y) + S(x, y-1) - S(x-1, y-1) + (ESM(x,y) == S) * E(x,y)
3. (x,y) 까지의 E, S, M를 누르는 경우의 수를 M(x,y)라 하면 M(x,y) = M(x-1, y) + M(x, y-1) - M(x-1, y-1) + (ESM(x,y) == M) * S(x,y)
4. answer = M(N, M)   
((x,y)까지의 = 모든 점 (i, j)에서의 (i <= x and j <= y), True = 1)

