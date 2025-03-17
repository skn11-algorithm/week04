# 큐2 (Deque 활용)

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])  # 큐에 값 추가
    elif cmd[0] == "pop":
        print(queue.popleft() if queue else -1)  # 큐에서 값 제거
    elif cmd[0] == "size":
        print(len(queue))  # 큐 크기 출력
    elif cmd[0] == "empty":
        print(0 if queue else 1)  # 비었는지 확인
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)  # 큐의 앞쪽 값 출력
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)  # 큐의 뒤쪽 값 출력

# 시간 복잡도: O(1), 각 연산 모두 O(1)