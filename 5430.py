# AC
# input: 테스트 케이스 수 T, 수행할 함수 p, 배열에 들어있는 수의 개수 n, 배열
# output: 각 테스트 케이스에 대해 입력으로 주어진 정수 배열에 함수를 수행한 결과 출력, 만약 에러 발생하면 error 출력
# r: 배열에 있는 수 뒤집기, d: 첫 번째 수 버리기 \ 빈 배열에 d 사용하면 에러 발생

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

while t>0:
    t -=1
    func = input()
    n = int(input())
    arr = input()
    
    flag = True
    queue = deque()
    for i in range(len(arr)):
        if arr[i].isdigit():
            queue.append(int(arr[i]))
    
    count = 0
    for f in func:
        if f == 'R':
            queue.reverse()
        elif f == 'D':
            count += 1
            if len(queue) == 0:
                flag = False
                break
            else:
                queue.popleft()
    
    if count > n or not flag:
        print('error') # 42를 위한 조건문
    elif flag:
        result = ','.join(map(str, queue))
        print(f'[{result}]')
    
    
