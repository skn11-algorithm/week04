# 부분수열의 합 (백트래킹)

import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0

def dfs(idx, total):
    global count
    if idx == N:
        if total == S:
            count += 1
        return
    dfs(idx + 1, total + nums[idx])  # 현재 숫자 포함
    dfs(idx + 1, total)  # 현재 숫자 포함 X

dfs(0, 0)
print(count if S != 0 else count - 1)  # 공집합 제외

# 시간 복잡도: O(2^N) (모든 부분집합을 탐색) 