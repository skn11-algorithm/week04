# 규칙 : 레이저가 나올 때 여는 괄호 개수만큼 추가
#      : )이 나왔을 때 직전이 (가 아니면 쇠막대기의 끝이므로 +1
import sys
X=sys.stdin.readline()

stack=[]
count=0
for i in range(len(X)):
    if X[i]=='(':
        stack.append('(')
    else:
        if X[i-1]=='(': # 직전이 열린 괄호. 레이저인 경우.
            stack.pop()
            count+=len(stack)
        else: # 직전이 닫힌 괄호. 쇠막대기의 끝.
            if stack:
                stack.pop()
                count+=1 # 쇠막대기 조각 추가.
print(count)



