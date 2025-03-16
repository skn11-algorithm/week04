# import sys
# from collections import deque
# input = sys.stdin.readline()

# n, m = map(int, input().split())

# que = deque([])
# for i in range(1, n+1):
#     que.append(i)
# lst = []
# lst.append(map(int, input().split()))
# count = 0
# for i in range(n):
    


# # [0] 뽑아내고 반환: popleft()
# # 왼쪽으로 한칸 이동: popleft, append()
# #오른쪽으로 한칸 이동: 오른쪽 제거 pop(), appendleft()

# https://jae-eun-ai.tistory.com/10
from collections import deque

n,m = map(int,input().split())
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 이런식으로 큐를 표현한다.
data = deque([i for i in range(1,n+1)])
#뽑아내려고 하는 수의 위치가 index변수에 순서대로 담아있다.
index = list(map(int,input().split()))

count = 0
for num in index:
    while 1:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= len(data)//2:
                data.rotate(-1)
                count += 1
            else:
                data.rotate(1)
                count += 1

print(count)