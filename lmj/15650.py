'''
입력 : N, M
출력 : 1~N까지 길이가 M 까지인 수열 세트 구하기
'''
# combination 사용
# from itertools import combinations

# n, m = map(int, input().split())

# for seq in combinations(range(1, n + 1), m):
#     print(' '.join(map(str, seq)))


# 백트래킹 사용
def backtrack(start, path):
    if len(path) == m:  # 길이가 m이면 출력
        print(' '.join(map(str, path)))
        return

    for i in range(start, n + 1):
        backtrack(i + 1, path + [i])  # i를 선택하고 다음 숫자로 이동

n, m = map(int, input().split())
backtrack(1, [])


