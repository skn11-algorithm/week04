# 최대공약수
# input: n1(개수) \n n1개의 양의 정수 \n n2(개수) \n n2개의 양의 정수
# output: A, B의 최대 공약수

import sys
import math

input = sys.stdin.readline

def multiply(n):
    num = list(map(int,input().split()))
    ans = 1
    for i in range(n):
        ans *= num[i]
    
    return ans

n1 = int(input())
a = multiply(n1)

n2 = int(input()) 
b = multiply(n2)

result = str(math.gcd(a,b))
if len(result) >= 10:
    print(result[len(result)-9]+result[len(result)-8]+result[len(result)-7]+result[len(result)-6]+result[len(result)-5]+result[len(result)-4]+result[len(result)-3]+result[len(result)-2]+result[len(result)-1])
else:
    print(result)
