### 1.1.1. 재귀 함수(Recursive Function)

def fib1(n: int): -> int:
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    

### 1.1.3. 메모이제이션(Memoization)

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # 기저조건

def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]



### 1.1.4. 메모이제이션 데코레이터(Memoization Decorator)

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)



### 1.1.5 간단한 피보나치 수열 (튜플 언패킹 & 스왑)

def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next 


if __name__ == "__main__":
    print(fib2(50))
    print(fib4(50))
    print(fib5(50))