# 문제
# 상근이는 학생들에게 두 양의 정수 A와 B의 최대공약수를 계산하는 문제를 내주었다. 그런데, 상근이는 학생들을 골탕먹이기 위해 매우 큰 A와 B를 주었다.
# 상근이는 N개의 수와 M개의 수를 주었고, N개의 수를 모두 곱하면 A, M개의 수를 모두 곱하면 B가 된다.
# 이 수가 주어졌을 때, 최대공약수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1000)이 주어진다. 둘째 줄에는 N개의 양의 정수가 공백으로 구분되어 주어진다. 이 수는 모두 1,000,000,000보다 작고, N개의 수를 곱하면 A가 된다.
# 셋째 줄에 M(1 ≤ M ≤ 1000)이 주어진다. 넷째 줄에는 M개의 양의 정수가 공백으로 구분되어 주어진다. 이 수는 모두 1,000,000,000보다 작고, M개의 수를 곱하면 B가 된다.

def divisors(x):    # 약수 찾는 함수 만들기
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0: 
            divisors.append(i)
    return divisors

def common_divisors(a, b):  # 공통 약수를 찾는 함수 만들기
    divisors_a = set(divisors(a)) 
    divisors_b = set(divisors(b)) 
    
    common_divisors = list(divisors_a & divisors_b) 
    common_divisors.sort()

