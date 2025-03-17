import math

#n 개의 수를 곱하면 a m 개의 수를 곱하면 b

n = int(input()) #개수
m = map(int,input().split())
a = math.prod(m) #곱 구하는 함수

k=int(input())
j = map(int,input().split())
b = math.prod(j)

print(str(math.gcd(a,b))[-9:])


