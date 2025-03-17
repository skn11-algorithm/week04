from collections import deque
import sys
input=sys.stdin.readline
queue=deque([])

N=int(input())

for _ in range(N):
    X=input().rstrip().split()
    if X[0]=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif X[0]=='size':
        print(len(queue))
    elif X[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif X[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif X[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif X[0]=='push':
        queue.append(int(X[1]))
