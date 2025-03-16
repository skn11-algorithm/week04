# import sys
# input = sys.stdin.readline
# n = int(input())
# lst = []
# for i in range(n):
#     m = input()
#     if 'push' in m:
#         a, k = m.split()
#         k = int(k)
#         lst.append(k)
#     if m == 'pop':
#         if len(lst) == 0:
#             k = -1
#         else:
#             k = lst.pop(0)
#         print(k)
#     if m == 'size':
#         k = len(lst)
#         print(k)
#     if m == 'empty':
#         if len(lst) == 0:
#             k = 1
#         else:
#             k = 0
#         print(k)
#     if m == 'front':
#         if len(lst) == 0:
#             k = -1
#         else:
#             k = lst[0]
#         print(k)
#     if m == 'back':
#         if len(lst) == 0:
#             k = -1
#         else:
#             k = lst.pop()
#             lst.append(k)
#         print(k)
# # ---
# # 시간 초과

# https://imzzan.tistory.com/4
import sys
from collections import deque
n = int(input())
queue = deque([])
for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])