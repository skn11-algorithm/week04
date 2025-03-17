# nCm= nPm/m! -> n!/m!(n-m)!
#팩토리얼 함수 사용
import math
n,m=map(int,input().split())

def ncr(n,m):
    return math.factorial(n) //( math.factorial(m) * math.factorial(n-m))

print(ncr(n,m))