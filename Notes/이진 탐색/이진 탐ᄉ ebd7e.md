# 이진 탐색(Binary Search)

## 순차 탐색(Sequential Search)

> 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 차례대로 확인하는 탐색 방법
> 

```python
def sequential_search(n, target, array):
	for i in range(n):
		if array[i] == target:
			return i + 1
	return False

n, target = 5, banana
array = [mango, banana, apple, melon, orange]

print(sequential_search(n, target, array))
```

> 순차 탐색은 보통 정렬되지 않은 리스트에서 사용한다.
리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 데이터를 찾을 수 있다.
리스트 등의 특정 원소의 개수를 세는 *count()* 함수도 순차 탐색을 사용한다.
> 

## 이진 탐색(Binary Search)

> 찾으려는 데이터와 중간점 위치의 데이터를 반복해서 비교하며 범위를 줄여나가는 탐색 방법
> 

```python
def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid + 1 #index는 0부터 시작하므로 +1
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

print (binary_search(array, target, 0, n-1))
```

<aside>
🔑 10 7⏎
1 3 5 7 9 11 13 15 17 19⏎
4

</aside>

> 이진 탐색은 한 번 탐색할 때마다 탐색해야하는 원소의 개수가 반으로 줄어들기 때문에 시간 복잡도가 $O(logN)$이다. 
이처럼 이진 탐색은 무척 빠르지만 정렬된 데이터에서만 사용할 수 있다.
> 

## Bisect

> 이진탐색 라이브러리
> 

```python
import bisect

array, target = [1,2,3,4,5], 3
print(bisect.bisect_left(array, target), end =', ')
print(bisect.bisect_right(array, target), end =', ')

array, target = [1,2,3,3,4,5], 3
print(bisect.bisect_left(array, target), end =', ')
print(bisect.bisect_right(array, target), end =', ')
```

<aside>
🔑 2, 3, 2, 4

</aside>

> 이진탐색을 이용하기 때문에 데이터가 정렬되어 있어야 한다.
bisect_left(array, target) : array에서 target의 왼쪽 인덱스를 구하기
bisect_right(array, target) : array에서 target의 오른쪽 인덱스를 구하기
>