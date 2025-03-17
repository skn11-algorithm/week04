# 회전하는 큐 (Deque)

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
dq = deque(range(1, N + 1))
count = 0

for target in targets:
    idx = dq.index(target)  # 현재 큐에서의 위치 찾기
    if idx <= len(dq) // 2:
        dq.rotate(-idx)  # 왼쪽으로 회전
        count += idx
    else:
        dq.rotate(len(dq) - idx)  # 오른쪽으로 회전
        count += len(dq) - idx
    dq.popleft()  # 첫 번째 원소 제거

print(count)  # 연산 횟수 출력

# 시간 복잡도: O(N × M) (M개의 숫자를 찾을 때 최대 N번 연산 가능)