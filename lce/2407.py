# 조합 (Big Integer 연산)

import sys
import math

n, m = map(int, sys.stdin.readline().split())
print(math.comb(n, m))  # 파이썬 내장 조합 함수 사용 (O(N))

# 시간 복잡도: O(N) (팩토리얼 연산)