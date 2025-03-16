# 회전하는 큐
# input: 큐의 크기 n, 수의 개수 m \n 뽑으려고 하는 수의 위치
# output: 문제의 정답 출력

from collections import deque

n,m = map(int, input().split())
dq = deque([i for i in range(1, n+1)])
index = list(map(int, input().split()))

count = 0

for i in index:
    while 1:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq)//2:
                dq.rotate(-1)
                count += 1
            else:
                dq.rotate(1)
                count += 1
                
print(count)