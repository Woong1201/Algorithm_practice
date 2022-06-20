# 위상 정렬(Topology Sort)

## 위상 정렬이란?

> 위상 정렬이란 방향 그래프의 모든 노드를 ‘방향성에 거스르지 않도록 순서대로 나열하는 것'이다.   
순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.
> 

## 진입차수(Indegree)

> 특정한 노드로 ‘들어오는’ 간선의 개수를 의미한다.
> 

## 위상 정렬 알고리즘

1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.   
    
![graph](https://user-images.githubusercontent.com/87896466/174576095-54b18db5-f2b2-48e3-9448-6ba34ae8881e.png)

위와 같은 그래프에서 위상 정렬 알고리즘을 적용해보자.

| 노드 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0 | 1 | 1 | 2 | 1 | 2 | 1 |

현재 진입차수가 0인 노드는 1이므로 1과 연결된 간선들을 지운다.   
![graph-2](https://user-images.githubusercontent.com/87896466/174576177-1dd120c2-88bf-4fda-a397-9854dfdd7db8.png)

| 노드 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0 | 0 | 1 | 2 | 0 | 2 | 1 |

그러면 2, 5 노드들이 진입차수가 0이 되었음을 알 수 있고, 그 노드들에 대하여 위의 과정을 다시 진행한다.

| 노드 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0 | 0 | 0 | 2 | 0 | 0 | 1 |

위 과정을 반복한다.

> 위상 정렬 알고리즘을 통해 얻게되는 진입차수가 0이되는 노드들의 순서가 위상 정렬을 수행한 결과이다.   
진입차수가 동시에 0이되는 노드들이 여러개 존재하면 여러 가지의 위상 정렬이 존재할 수 있다.   
예시에서는 1-2-5-3-6-4-7, 1-5-2-3-6-4-7 등의 위상 정렬이 존재한다.   
> 

## 위상 정렬 알고리즘 구현

```python
from collections import deque
import sys

v, e = map(int, sys.stdin.readline().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	indegree[b] += 1

def topology_sort():
	result = []
	queue = deque()

	for i in range(1, v+1):
		if indegree[i] == 0:
			queue.append(i)

	while queue:
		now = queue.popleft()
		result.append(now)
		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				queue.append(i)

	print(*result)

topology_sort()
```

> 모든 노드들을 방문하기 전에 위상 정렬 알고리즘이 종료되었다면 사이클이 발생했다고 판단할 수 있다.   
위상 정렬의 시간 복잡도는 O(V+E)이다.
>
