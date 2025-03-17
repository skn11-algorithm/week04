'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령 처리
push, pop, size, empty, front, back
'''

import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for i in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        que.append(int(com[1]))

    elif com[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.popleft()

    elif com[0] == 'size':
        print(len(que))

    elif com[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif com[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    elif com[0] == 'back':
        if len(que) == 0:
            print(-1)
        else: 
            print(que[-1])