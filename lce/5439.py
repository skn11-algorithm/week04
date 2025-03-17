# AC (덱)

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1]
    dq = deque(arr.split(',')) if n else deque()
    rev = False

# 시간 복잡도: O(N) (R 연산을 최적화하여 O(N) 유지)
