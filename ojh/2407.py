# nCm
# n!/(n-m!)m!
# n-m+1 ~ n 까지 / m!

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
result=1
for i in range(1,m+1):
    result*=(n-m+i)
    result//=i
print(result)