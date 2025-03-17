import sys
from collections import deque

input=sys.stdin.readline
N,M=map(int,input().split())
queue=deque([i for i in range(1,N+1)])
targets=deque(list(map(int,input().split())))

count=0
for target in targets:
    if target==queue[0]:
        queue.popleft()
    else:
        idx=queue.index(target)
        if idx<=len(queue)-idx: # idx만큼 오른쪽으로
            for i in range(idx):
                queue.append(queue.popleft())
                count+=1
        else: # len(queue)-idx만큼 오른쪽으로
            for i in range(len(queue)-idx):
                queue.appendleft(queue.pop())
                count+=1
        
        queue.popleft()
print(count)