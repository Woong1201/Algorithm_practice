# 다이나믹 프로그래밍(Dynamic Programming)

## 다이나믹 프로그래밍이란?

> 동적 계획법이라고도 불리는 다이나믹 프로그래밍은 문제를 작은 문제들로 나누어 해결하는 풀이방법이다.   
이때, 작은 문제들의 해답들을 저장해두고, 큰 문제를 해결하는데에 사용한다.
> 

## Recursive Fibonacci

```python
N = int(input())

def fibonacci(x):
	if x == 1 or x == 2:
		return 1
	return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(N))
```

<aside>    
30⏎    
  
🔑 832040    

</aside>

> 위의 코드에서 f(6)을 호출하면 아래처럼 많은 수의 계산을 해야한다.   
f(6) = f(5)+f(4) = (f(4)+f(3))+(f(3)+f(2)) = ((f(3)+f(2))+(f(2)+f(1)))+((f(2)+f(1))+f(2)) = ...   
N이 커질 수록 기하급수적으로 많은 연산을 하게 되며,   
N = 100일때, 약 1,000,000,000,000,000,000,000,000,000,000번의 연산을 해야 한다.   
반복되는 연산때문인데, 이를 Dynamic Programming으로 해결할 수 있다.   
> 

## Memoization(Caching)기법의 Recursive Fibonacci

```python
N = int(input())
memo = [0] * (N + 1)

def fibonacci(x):
    if x == 1 or x == 2:
        memo[x] = 1
    if memo[x] == 0:
        fibonacci(x - 1)
        memo[x] = memo[x-1] + memo[x-2]
    return (memo[x])

print(fibonacci(N))
```

<aside>
100⏎    
  
🔑 218922995834555169026     

</aside>

> 기본 Recursive Fibonacci에서는 N = 100의 연산을 해결할 수 없었다.   
O(2<sup>N</sup>)의 시간복잡도를 가지기 때문인데 컴퓨터가 1초에 1억번의 연산을 한다고 해도 100억년이 걸린다.   
하지만 Memoization 기법의 코드는 O(N)의 시간복잡도를 가진다.   
f(6) = f(5)+~~f(4)~~ = (f(4)+~~f(3)~~)+~~f(4)~~ = ((f(3)+~~f(2)~~)+~~f(3)~~)+~~f(4)~~ = (((~~f(2)~~+~~f(1)~~)+~~f(2)~~)+~~f(3)~~)+~~f(4)~~   
취소선이 있는 함수들의 연산은 memo 리스트에 저장되어 있어 추가로 연산을 하지 않기 때문이다.   
위와 같은 방식을 큰 문제를 해결하기 위해 작은문제를 호출한다고 하여 Top-Down방식이라고 한다.   
> 

## Iterative Fibonacci

```python
N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1);
	dp[i] = dp[i-1] + dp[i-2]

print(dp(N))
```

<aside>
100⏎    
  
🔑 218922995834555169026   

</aside>

> 위의 방식은 작은 문제부터 차근차근 답을 도출한다고 하여 Bottom-up 방식이라고 한다.   
이에 사용되는 결과 저장용 리스트는 DP 테이블 이라고 부른다.   
재귀 방식은 ‘recursive depth error’가 발생할 수 있으므로 Iterative 방식을 사용하도록 하자.   
sys 라이브러리의 setrecursionlimit()로 재귀 제한을 완화할 수 있다.   
>
