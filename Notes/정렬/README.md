# 정렬(Sorting)


## 정렬(Sorting)이란?

> 데이터를 특정한 기준에 따라 순서대로 나열하는 것.
> 

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 |
| --- | --- | --- |
| 선택 정렬 | *O(N<sup>2</sup>)* | *O(N)* |
| 삽입 정렬 | *O(N<sup>2</sup>)*  | *O(N)* |
| 퀵 정렬 | *O(NlogN)* | *O(N)* |
| 계수 정렬 | *O(N+K)* | *O(N+K)* |

## 선택 정렬(Selection Sort)

> 가장 작은 데이터를 ‘선택’해서 정렬되지 않은 데이터 중 가장 앞의 데이터와 위치를 바꿔 정렬한다.
> 

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i
	for j in range(i+1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[j] = array[j], array[i]

print(array)
```

<aside>
🔑 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

</aside>

> 가장 작은 데이터를 앞으로 보내는 과정을 반복해서 수행하게 되면, 전체 데이터의 정렬이 이루어진다.   
정렬되지 않은 부분의 전체를 순회하며 가장 작은 데이터의 위치를 min_index에 저장한 뒤,   
순회가 끝났을 때 정렬되지 않은 부분의 가장 앞의 데이터와 min_index의 데이터의 위치를 바꾼다.


## 삽입 정렬(Insertion Sort)

> 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하여 정렬한다.
> 

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
		else:
			break

print(array)
```

<aside>
🔑 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

</aside>

> 삽입 정렬 과정 중 각 원소의 자리를 찾으면 탐색을 바로 멈춘다.   
삽입 정렬도 선택 정렬과 마찬가지로 *O(N<sup>2</sup>)* 의 시간복잡도를 가지지만,    
위의 특성 때문에 데이터가 거의 정렬되어 있는 경우에는 *O(N)*의 시간복잡도를 가진다.
> 

## 퀵 정렬(Quick Sort)

> 피벗(pivot)이라는 교환하기 위한 기준을 통해 정렬한다.
> 

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		while left <= end and array[left] <= array[pivot]:
			left += 1
		while right > start and array[right] >= array[pivot]:
			right -= 1
		if left > right:
			array[right], array[pivot] = array[pivot], array[right]
		else:
			array[right], array[left] = array[left], array[right]
	quick_sort(array, start, right-1)
	quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```

<aside>
🔑 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

</aside>

## 계수 정렬(Count Sort)

> 주어진 데이터를 모두 담을 수 있는 배열을 만들어 정렬한다.
> 

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in range(len(array)):
	count[array[i]] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end = ' ')
```

<aside>
🔑 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9

</aside>
 
> 계수 정렬은 주어진 데이터를 담을 수 있는 배열을 만들어 사용하기 때문에 데이터가 계수 정렬을 사용하기에 적절한 조건을 만족하는지 알아야 사용가능하다.   
데이터의 크기가 한정되어 있고, 데이터가 많이 중복되어 있을때 유리하다.
> 

## 정렬 라이브러리

```python
array.sort()
sorted(array)
```

> 각 언어는 이미 잘 작성된 기본 정렬 라이브러리를 가지고 있기 때문에, 직접 구현해야 하는 경우가 아니면 이를 잘 활용하면 된다.
