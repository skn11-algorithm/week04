'''
첫째줄 연산개수 N
둘째줄 : 연산에 대한 정보 (x가 자연수라면 x append, 0이라면 min값 출력 후 pop)
'''
import sys
import heapq

n = int(sys.stdin.readline())
heap = [] # 배열

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:

        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    # x가 0이 아니라면 배열에 x를 힙 푸시
    else:
        heapq.heappush(heap, x)