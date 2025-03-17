n, m = map(int, input().split())
# n: 범위, m: 수열 갯수

# for i in range(1, n+1):
#     for j in range(2, n+1):
#         if i<j and j<n+1:
#             print(i, j)


# https://jiwon-coding.tistory.com/22
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)