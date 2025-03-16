# import sys
# import ast

# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#     try:
#         k = list(input()[i: i+1] for i in range(len(input()))) # 명령
#         m = int(input())    #갯수
#         lst = ast.literal_eval(input())       # 행렬 인풋
#         l = list(input()[i: i+1] for i in range(len(input())))         # 수행 명령
#         if len[lst] != m:
#             print('error')
#         for i in k:
#             if i == 'R':
#                 lst = lst[-1::-1]
#             elif i == 'D':
#                 lst.pop(0)
#             else:
#                 print('error')
#                 break
#         for i in l:
#             if i == 'R':
#                 lst = lst[-1::-1]
#             elif i == 'D':
#                 lst.pop(0)
#             else:
#                 print('error')
#                 break
#         print(lst)        
#     except ValueError:
#         print('error')
#     except TypeError:
#         print('error')

    
# https://hongcoding.tistory.com/44
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")