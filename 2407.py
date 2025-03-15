a, b = map(int, input().split())
a_mul = 1
b_mul = 1
ba_mul = 1
for i in range (1, a+1):
    a_mul = a_mul * i

for i in range(1, b+1):
    b_mul = b_mul * i

for i in range (1, a - b + 1):
    ba_mul = ba_mul * i

# print(int(a_mul / b_mul / ba_mul)) 실수 나눗셈으로 오차 발생 가능
print(int(a_mul // b_mul // ba_mul))