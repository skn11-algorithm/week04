'''
# 골드바흐 파티션 
# 입력 : 테스트 케이스의 수
# 출력 : 소수끼리 합쳐 테스트케이스가 되는 수

# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
'''

import sys

def is_prime(num):
    if num < 2:  # 0과 1은 소수가 아님
        return False
    if num == 2:  # 2는 유일한 짝수 소수
        return True
    if num % 2 == 0:  # 2를 제외한 짝수는 소수가 아님
        return False
    for p in range(3, int(num**0.5) + 1, 2):  # 3부터 홀수만 검사하여 연산량 절약
        if num % p == 0:
            return False
    return True

T = int(sys.stdin.readline().strip())

for _ in range(T):  # 반복 변수를 사용하지 않으므로 `_` 사용
    n = int(sys.stdin.readline().strip())

    if n % 2 != 0:  # 예외적으로 홀수가 들어올 경우 무시 (골드바흐의 추측은 짝수만 적용됨)
        continue

    a, b = n // 2, n // 2  # 중간값에서 시작

    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1
