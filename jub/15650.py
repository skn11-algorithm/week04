
n, m = map(int, input().split())
s = [] #숫자 저장할 리스트 있어야 됨됨

def dfs(start):  # 함수에 매개변수 추가
    if len(s) == m: #만약 s리스트의 길이가 m과 같으면 조건 만족
        print(' '.join(map(str, s))) #공백구분,s 리스트는 문자열로 반환환
        return
    for i in range(start, n+1):  # 시작점 변경
        s.append(i) #s리스트에 현재숫자 i추가가
        dfs(i+1)  # 다음 숫자부터 탐색
        s.pop() #백트래킹: 현재 숫자를 제거하고 다른 조합 탐색색

dfs(1)  # 1부터 시작하여 함수 호출 

