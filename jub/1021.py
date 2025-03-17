# 첫번째 원소 뽑음 
# 왼쪽으로 한칸 이동 
# 오른쪽으로 한칸 이동

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split()) #큐 크기, 뽑아낼 개수
targets = list(map(int,sys.stdin.readline().split()))
dq = deque(range(1,n+1))
count = 0 # 이동 횟수 저장


for target in targets:
    index = dq.index(target)  # 현재 큐에서 목표 숫자의 위치

    # 왼쪽으로 이동하는 게 빠른 경우
    if index < len(dq) - index:
        while dq[0] != target:
            dq.append(dq.popleft())  # 왼쪽으로 이동
            count += 1
    # 오른쪽으로 이동하는 게 빠른 경우
    else:
        while dq[0] != target:
            dq.appendleft(dq.pop())  # 오른쪽으로 이동
            count += 1

    dq.popleft()  # 목표 숫자 제거

print(count)  # 총 이동 횟수 출력