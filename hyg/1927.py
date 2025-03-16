# 최소힙
# input: 연산의 개수n, 연산에 대한 정보를 나타내는 정수 x
# output: 0의 개수만큼 답을 출력, 배열이 빈 경우 0 출력

# x가 자연수면 배열에 x를 추가, x가 0이면 배열에서 가장 작은 값을 출력하고 배열에서 그 값 제거

import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    a = int(input())
    
    if a != 0:
        heapq.heappush(heap, a)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
            