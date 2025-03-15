# import sys
# input = sys.stdin.readline

# n = int(input())
# lsta = [int(x) for x in input.split()]
# m = int(input())
# lstb = [int(x) for x in input.split()]
# A = 1
# B = 1
# for i in lsta:
#     A  = A * i

# for i in lstb:
#     B = B * i
# a = max(A, B) 
# b = min(A, B) 
# # 유클리드 호제법

# while b != 0:
#     a , b == a // b, a % b

# if 99999999 < b:
#     b = str(b)
#     print(b[-9:])
# else:
#     print(b)

# 런타임 에러(AttributeError)

def gcd(a, b):
    while b!=0:
        t = b
        b = a%b
        a = t
    return a
input()
x = input().split()
a=1
for k in x: a *= int(k)
input()
x = input().split()
b=1
for k in x: b *= int(k)
print(str(gcd(a,b))[-9:])