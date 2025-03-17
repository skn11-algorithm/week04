import sys
from collections import deque

def ac_func(AC,queue):
    reverse_flag = False  
    for ac in AC:
        if ac=="R":
            reverse_flag=not reverse_flag
        elif ac=='D':
            if len(queue)==0:
                print("error")
                return # 에러 발생 시 바로 종료
            else:
                if reverse_flag:
                    queue.pop()
                else:
                    queue.popleft()
                    
    if reverse_flag:
        queue.reverse()
    print("["+",".join(list(queue))+"]")


input=sys.stdin.readline
N=int(input())

for _ in range(N):  
    AC=input()
    d=int(input())
    arr=input().strip()[1:-1]
    arr=deque(arr.split(',') if arr else [])
    ac_func(AC,arr)