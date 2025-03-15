# n = int(input())
# lst=[]
# for i in range(n):
#     lst.append(int(input()))

# prime = [True] * 100001
# prime[0:2] = [False, False]
# k = int(10000**0.5+1)

# # 소수 찾기
# for i in range(k):
#     if i == 0:
#         continue
#     for j in range(2, 100):
#         if prime[i] == True:
#             prime[i*j] = False

# #골드바흐 -> 차이가 가장 작은 값 찾기 실패
# for i in lst:
#     for j in range(2, i):
#         k = i - j
#         if k < 0:
#             continue
#         if prime[j] ==True and prime[k] == True:
#             print(k, j)
#             break

#https://blognavercomcheetah254.tistory.com/48
import math

def d(N): # 소수 판별 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True
    
N = int(input()) # 테스트 케이스 수 입력

for _ in range(N):
    num = int(input()) # 짝수 입력
    
    A = num // 2 # 두 수 중 줄어드는 변수
    B = num // 2 # 두 수 중 늘어나는 변수
    
    for _ in range(num // 2):
        if d(A) and d(B): # 두 수가 소수이면 출력
            print(A, B)
            break
        else: # 소수가 아니면 두 수를 줄이고 늘리기
            A -= 1
            B += 1