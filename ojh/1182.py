# 주어진 수열에서 합이 S가 되는 모든 부분 수열을 찾는 백트래킹 알고리즘
import sys
input=sys.stdin.readline

N,S=map(int,input().split())
su=list(map(int,input().split()))

count=0 # 조건을 만족하는 부분 수열의 개수를 저장할 변수
def backtracking(idx,sum):
    global count
    # idx>0 이 없다면
    # backtracking(0, 0)이 실행되자마자 sum == S 만족하므로 공집합이 정답으로 카운트됨
    if idx > 0 and sum==S: # 현재 선택한 원소들의 합이 S라면 count 증가
        count+=1
    for i in range(idx,N): # 현재 인덱스부터 탐색
        # idx 이후의 원소들만 선택하여 중복 탐색을 방지
        backtracking(i+1,sum+su[i]) # 현재 숫자를 더한 후 다음 단계 진행

backtracking(0,0)
print(count)

#-7 -3 -2 5 8
#0,0
#1,-7
#2,-10
#3,-12
#4,-7
#5,1  하지만 sum이 S=0이 아니므로 종료
###################
# 남은 for문들..
# backtracking(3, -12)의 for 루프 계속 진행
# for문에서 i가 4가 아니라 5선택
# 3,-12 -> 5,-4 # 종료
# backtracking(2, -10)의 for 루프 계속 진행
# i가 3이 아니라 4 선택
# 2,-10 -> 4,-5 -> 5,3 종료
#       -> 5,-2 종료
# backtracking(1, -7)의 for 루프 계속 진행
# i가 2가 아니라 3 선택
# (3,-9) -> ,,, 
# ,,,
# backtracking(0,0)의 for 루프 계속 진행
# i가 0이 아니라 1 선택
# (1,-3) -> ,,