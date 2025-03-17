# 부분수열의 합
# input: 정수의 개수 n  정수 s \n n개의 정수는 빈칸을 사이에 두고 주어짐
# output: 합이 s가 되는 부분 수열의 개수 구하기

# 생각흐름
# 백트래킹으로 모든 경우 다 계산하기

import sys

def backtracking(index, result):
    global cnt
    
    if index >= n:
        return
    
    result += numbers[index]
    
    if result == s:
        cnt+=1
    
    backtracking(index+1, result) # 현재 index에 정수를 더한 것
    backtracking(index+1, result - numbers[index])  # 현재 index에 정수를 더하지 않은 것
 
input = sys.stdin.readline

n,s = list(map(int, input().split()))
numbers = list(map(int, input().split()))
cnt = 0

backtracking(0,0)
print(cnt)
