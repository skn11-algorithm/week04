# nCm= nPm/m! -> n!/m!(n-m)!
import math
n,m=map(int,input().split())
# #팩토리얼 함수 
# def fa(x):
#     if x == 1: #팩토리얼의 기본 조건이 x=1 일 때 1 반환환
#         return 1
#     else:
#         return math.factorial(x)
def ncr(n,m):
    return math.factorial(n) //( math.factorial(m) * math.factorial(n-m))

print(ncr(n,m))