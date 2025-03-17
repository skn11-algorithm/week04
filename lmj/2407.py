'''
combination 구하기 nCm
'''


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
n, m = map(int, input().split())
print(factorial(n) // (factorial(n-m) * factorial(m)))
