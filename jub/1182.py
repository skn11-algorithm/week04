
n,s = map(int,input().split()) #n=숫자개수,s=목표합
m =list(map(int,input().split())) #숫자리스트
a = [] # 저장받을 리스트
cnt = 0 #경우의 수 카운트, 조건 만족

# 양수만 고르기
# 양수 고른 원소를 더한 값이 s가 되어야 함
def sol(start):
    global cnt #전역변수 수정하기 위함 
    if sum(a) == s and len(a) > 0:
        cnt += 1

    for i in range (start,n):
        a.append(m[i])
        sol(i+1)
        a.pop()

sol(0)
print(cnt)

