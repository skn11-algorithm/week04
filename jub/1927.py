import sys
import heapq

n= int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) == 0: #힙이 비어있으면 0 출력
            print(0)
        else:
            print(heapq.heappop(heap)) #최소값 출력 
    else:
        heapq.heappush(heap,x) # x>0이면 힙에 값 추가