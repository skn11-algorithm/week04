# 힙 => 우선순위 큐 => 완전 이진트리의 일종
# 여러값 중 최대/최소 값을 빠르게 찾아내도록 만들어진 반정렬 상태
# O(N) -> 힙에서 최대/최소값 찾기 : O(logN)

# 자연수면 추가
# 0이면 최소값 출력&제거

import heapq
import sys
input=sys.stdin.readline
heap=[]
N=int(input())

for _ in range(N):
    x=int(input())
    if x==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)