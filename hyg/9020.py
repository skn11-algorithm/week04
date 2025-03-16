# input: 테스트 케이스 수 T \n 짝수들 n
# output: 주어진 n의 골드바흐 파티션 출력 (작은 것부터, 공백으로)
# 골드바흐 파티션: 짝수를 두 소수의 합으로 나타내는 표현 \ 두 소수의 차이가 가장 작은 것

# 1. n = input
# 2. 에라토스테네스의 체
# 3. 두 소수의 차이가 가장 작은 걸 출력하는 코드 작성하기

import sys
import math

input = sys.stdin.readline

def goldbach(num):
    prime = [True for _ in range(0, num + 1)]
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(num)+1)):
        if prime[i]:
            for j in range(i*i, num+1,i):
                prime[j] = False

    min1 = min2 = 0
    temp = 1233456789
    for i in range(3, num):
        if prime[i] and prime[num-i] and temp > abs(num-i-i):
            temp = abs(num-i-i)
            min1 = i
            min2 = num-i
    
    return min1, min2

n = int(input())

for i in range(n):
    num = int(input())
    num1, num2 = goldbach(num)
    print(num1, num2)


