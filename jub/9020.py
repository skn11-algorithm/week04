import math

def soe(n): # 소수 판별 함수
    if n == 1: # 1은 소수가 아님
        return False
    for i in range(2, int(math.sqrt(n))+1): # 2부터 제곱근까지 수로 나눔눔
        if n % i == 0: #나누어 떨어지는 수가 있으면 소수 아님님
            return False
    return True

n = int(input()) # 테스트 케이스 수 입력

for _ in range(n):
    num = int(input()) # 짝수 입력

    A = num // 2 # 작은 수
    B = num // 2 # 큰 수

    while A > 0:
        if soe(A) and soe(B): #두수가 소수면 출력 함함
            print(A, B)
            break
        A -= 1 # A는 줄여가면서 검사
        B += 1 #B는 증가시키면서 검사



        

