# 최소힙 (Heapq )

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heapq.heappop(heap) if heap else 0)  # 최소값 출력 및 삭제
    else:
        heapq.heappush(heap, x)  # 최소 힙에 추가

# 시간 복잡도: O(N log N) (heapq의 삽입/삭제 연산이 O(log N))