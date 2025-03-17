''' 
매우 큰 최대공약수 구하기
'''

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

n_num = 1 # 각 리스트 그룹의 숫자곱을 초기화
m_num = 1 # 각 리스트 그룹의 숫자곱을 초기화

for i in n_list:
	n_num *= i
      
for i in m_list:
	m_num *= i

print(str(gcd(n_num,m_num))[-9:]) 