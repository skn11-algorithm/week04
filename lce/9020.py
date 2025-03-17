# 골드바흐의 추측 (에라토스테네스의 체)

import sys

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

primes = sieve(10000)
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    for a in range(n // 2, 1, -1):
        if primes[a] and primes[n - a]:
            print(a, n - a)
            break
# 시간 복잡도: O(N log log N) (소수 판별) + O(N) (탐색)