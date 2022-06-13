# 크루스칼 알고리즘(Kruskal Algorithm)

## 신장 트리(Spanning Tree)

> 하나의 그래프에 있는 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프이다.
이때, 위의 조건이 트리의 조건과 같기 때문에 신장트리라고 부르는 것이다.
따라서 트리 구조의 특징인 “(간선의 개수) = (노드의 개수) - 1”을 가진다.
> 

## 크루스칼 알고리즘

> 주어진 그래프에서 최소한의 비용으로 신장트리를 찾을때 이용하는 알고리즘 중 하나이다.
모든 간선들에 대하여 정렬한 뒤, 가장 거리가 짧은 간선부터 집합에 포함시킨다.
따라서 그리디 알고리즘으로 분류된다.
> 

## 크루스칼 알고리즘 원리

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    1. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    2. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
3. 모든 간선에 대하여 위의 과정을 시행한다.   
![graph-3](https://user-images.githubusercontent.com/87896466/173347146-ad7ce838-c6d0-44a7-bd11-e01dcbf9f8fa.png)
    

위와 같이 주어진 그래프에서 최소 신장 트리를 찾아보자.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
    
    
    | 간선 | (1,3) | (4,7) | (4,6) | (6,7) | (1,2) | (2,6) | (2,3) | (5,6) | (1,5) |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | 비용 | 7 | 13 | 23 | 25 | 29 | 34 | 35 | 53 | 75 |
2. 간선을 확인하며 트리에 포함시킬지 선택한다.
    
    
    | 간선 | (1,3) | (4,7) | (4,6) | (6,7) | (1,2) | (2,6) | (2,3) | (5,6) | (1,5) |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | 비용 | 7 | 13 | 23 | 25 | 29 | 34 | 35 | 53 | 75 |
    | 트리 | o | o | o | x | o | o | x | o | x |
    
    (1,3), (4,7), (4,6) 간선까지 확인한 신장 트리의 상태는 다음과 같다.   
    ![graph-2](https://user-images.githubusercontent.com/87896466/173347276-6cb1f920-15af-4b37-aed4-c57d393757db.png)
    
    이때, (6,7) 간선은 사이클을 발생시키므로 신장 트리에 포함하지 않게 된다.
    
3. 크루스칼 알고리즘의 결과
    
    위의 과정을 진행하면 아래와 같은 최소 신장 트리를 얻을 수 있다.     
    ![graph](https://user-images.githubusercontent.com/87896466/173347366-c8141607-0583-4976-b384-d41c4d669022.png)
    
    위의 예시에서 최소 신장 트리의 비용은 159이다.
    

## 크루스칼 알고리즘 구현

```python
import sys

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
	parent[i] = i

for _ in range(e):
	edges.append(tuple(map(int, sys.stdin.readline().split())))

edges.sort(key = lambda x : x[2])

for edge in edges:
	a, b, cost = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

print(result)
```



> 크루스칼 알고리즘은 간선의 개수가 E개일 때, O(ElogE)의 시간복잡도를 갖는다.   
시간이 가장 오래 걸리는 부분이 간선을 정렬하는 작업이기 때문이다.
>
