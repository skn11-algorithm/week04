# 큐2
# input: 명령의 수 n \n 명령이 하나씩 주어짐
# output: 출력해야 하는 명령이면 하나씩 출력

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    command = list(input().split())
    
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])