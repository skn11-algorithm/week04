'''
입력 : N, S'
출력 : N개의 수들 중 합이 S가 되는 수열 갯수

'''
N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []

def solve(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1

    for i in range(start, N):
        ans.append(num[i])
        solve(i+1)
        ans.pop()

solve(0)
print(cnt)


