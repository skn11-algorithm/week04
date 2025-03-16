# input: n,m
# output: 문제의 조건을 만족하는 수열을 한 줄에 하나씩 출력
# 문제: 1부터 n까지 자연수 중 중복 없이 m개를 고른 수열 \ 수열은 오름차순
# 저번 문제랑 다른 점: 중복 없이!!

import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))

arr = []

def backtracking():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()


backtracking()
