import sys
sys.setrecursionlimit(10**6) #Python이 정한 최대 재귀 갚이를 변경 가능
input=sys.stdin.readline

def gcd(A,B):
    if B==0:
        return A
    return gcd(B,A%B)


a,b=1,1
input()
A=input().split()
for i in A : a*=int(i)
input()
B=input().split()
for i in B : b*=int(i)

a,b= (a,b) if a>b else (b,a)
print(str(gcd(a,b))[-9:]) #만약, 9자리보다 길다면, 마지막 9자리만 출력