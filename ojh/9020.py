import sys

is_prime=[False,False]+[True]*(100000-1)
def prime(n): # 소수의 배수는 소수가 아님
    n_sqrt=int(n**0.5)
    for i in range(2,n_sqrt):
        if is_prime[i]==True: # 이미 소수가 아님이 판별된 숫자는 건너뛰면서 성능 개선선
            for j in range(i*i,n,i):
                is_prime[j]=False
            
input=sys.stdin.readline
n=int(input())
prime(100000)

for i in range(n):
    num=int(input())   
    for j in range(num//2,1,-1):
        # 두 소수의 차이가 가장 작은 것을 출력
        if is_prime[j] and is_prime[num-j]:
            print(j,num-j) 
            break
