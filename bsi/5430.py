# AC
# input: 테스트 케이스 수 T, 수행할 함수 p, 배열에 들어있는 수의 개수 n, 배열
# output: 각 테스트 케이스에 대해 입력으로 주어진 정수 배열에 함수를 수행한 결과 출력, 만약 에러 발생하면 error 출력
# r: 배열에 있는 수 뒤집기, d: 첫 번째 수 버리기 \ 빈 배열에 d 사용하면 에러 발생

# reverse를 계속 수행하는 것 때문에 시간초과 발생하는 것 같음

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    func = input()
    n = int(input())
    xs = input()[1:-2].split(',') # 인덱스 유념해서 잘라야함
    
    r = 0
    flag = True
    
    # n==0이면 empty deque
    if n == 0:
        queue = deque()
    else:
        queue = deque(xs)
    
    for f in func:
        if f == 'R':
            r += 1
        elif f == 'D':
            if len(queue) == 0:
                print('error')
                flag = False
                break
            else:
                if r % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
    
    if flag:
        if r % 2 == 1:
            queue.reverse()
        result = ','.join(map(str, queue))
        print(f'[{result}]')
    
    
    
