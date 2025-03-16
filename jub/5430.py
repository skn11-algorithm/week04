import sys
from collections import deque

def ac_function(p, arr):
    dq = deque(arr)  # 배열을 deque로 변환 (O(1))
    reverse = False  # 뒤집기 상태 관리 변수

    for cmd in p:  # 명령어 순회
        if cmd == 'R':
            reverse = not reverse  # 뒤집기 상태 변경
        elif cmd == 'D':
            if not dq:  # deque가 비어 있으면 error 출력
                return "error"
            if reverse:
                dq.pop()  # 뒤집힌 상태라면 뒤에서 제거
            else:
                dq.popleft()  # 일반 상태라면 앞에서 제거

    # 최종 결과 정리 (뒤집기 상태일 경우 한 번만 뒤집음)
    result = list(dq)
    if reverse:
        result.reverse()

    return "[" + ",".join(map(str, result)) + "]"

# 입력 처리
t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

for _ in range(t):
    p = sys.stdin.readline().strip()  # 명령어 문자열
    n = int(sys.stdin.readline().strip())  # 배열 길이
    arr_input = sys.stdin.readline().strip()  # 배열 입력

    # 배열이 비어있을 경우 예외 처리
    arr = deque(map(int, arr_input[1:-1].split(","))) if n > 0 else deque()

    print(ac_function(p, arr))  # 결과 출력
