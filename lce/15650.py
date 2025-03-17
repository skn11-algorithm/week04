# N과 M (2) (백트래킹)

import sys

N, M = map(int, sys.stdin.readline().split())

def dfs(start, path):
    if len(path) == M:
        print(*path)
        return
    for i in range(start, N + 1):
        dfs(i + 1, path + [i])  # 중복 없이 증가하는 조합 탐색

dfs(1, [])

# 시간 복잡도: O(2^N) (모든 조합 탐색)